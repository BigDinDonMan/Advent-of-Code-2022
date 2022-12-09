

using System.Diagnostics.CodeAnalysis;

public struct Vector2 {
    public int X { get; set; }
    public int Y { get; set; }

    public Vector2(int x, int y) => (X, Y) = (x, y);

    public Vector2 Abs() => new Vector2(Math.Abs(X), Math.Abs(Y));

    public static Vector2 operator+(Vector2 first, Vector2 second) => new(first.X + second.X, first.Y + second.Y);
    public static Vector2 operator-(Vector2 first, Vector2 second) => new(first.X - second.X, first.Y - second.Y);

    public override bool Equals([NotNullWhen(true)] object obj) => obj is Vector2 v ? v.X == X && v.Y == Y : false;

    public override int GetHashCode() => X.GetHashCode() ^ 17 + Y.GetHashCode();

    public override string ToString() => $"({X}, {Y})";
}