using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

public class Program
{
	static bool IsTailTouchingHead(Vector2 headPosition, Vector2 tailPosition) {
		var diff = headPosition - tailPosition;
		var diffAbs = diff.Abs();
		return diffAbs.X <= 1 && diffAbs.Y <= 1;
	}

	static (Vector2, int) GetMoveData(string inputLine) {
		var split = inputLine.Split();
		var dirStr = split[0];
		var distanceStr = split[1];
		var distance = Int32.Parse(distanceStr);
		var directionVec = dirStr switch {
			"R" => new Vector2(1, 0),
			"L" => new Vector2(-1, 0),
			"U" => new Vector2(0, 1),
			"D" => new Vector2(0, -1),
			_ => throw new InvalidOperationException("Wrong direction provided")
		};
		return (directionVec, distance);
	}

	static Vector2 GetKnotMoveVector(Vector2 knot) {
		return new Vector2(
			Math.Clamp(knot.X, -1, 1),
			Math.Clamp(knot.Y, -1, 1)
		);
	}

	static void Part1(string[] lines) {
		var visited = new Dictionary<Vector2, bool>();
		var headPosition = new Vector2();
		var tailPosition = new Vector2();
		visited[tailPosition] = true;
		foreach (var line in lines) {
			var (directionVec, distance) = GetMoveData(line);
			for (int i = 0; i < distance; ++i) {
				headPosition += directionVec;
				if (!IsTailTouchingHead(headPosition, tailPosition)) {
					var diff = headPosition - tailPosition;
					tailPosition += GetKnotMoveVector(diff);
				}
				visited[tailPosition] = true;
			}
		}

		var result = visited.Where(pair => pair.Value).Count();
		Console.WriteLine($"Result: {result}");
	}

	static void Part2(string[] lines) {
		var visited = new Dictionary<Vector2, bool>();
		var knotPositions = new Vector2[10];
		ref Vector2 headPosition = ref knotPositions[0];
		ref Vector2 tailPosition = ref knotPositions[9];
		visited[tailPosition] = true;
		foreach (var line in lines) {
			var (directionVec, distance) = GetMoveData(line);
			for (int i = 0; i < distance; ++i) {
				headPosition += directionVec;
				for (int j = 1; j < knotPositions.Length; ++j) {
					if (!IsTailTouchingHead(knotPositions[j - 1], knotPositions[j])) {
						var diff = knotPositions[j - 1] - knotPositions[j];
						knotPositions[j] += GetKnotMoveVector(diff);
					}
				}
				visited[tailPosition] = true;
			}
		}

		var result = visited.Where(pair => pair.Value).Count();
		Console.WriteLine($"Result: {result}");
	} 

	public static void Main(string[] args)
	{
        var input = File.ReadAllLines("input.txt");
		Part1(input);
		Part2(input);
	}
}