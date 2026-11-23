namespace Names;

// 依 wiki/first-app（官方 Names 教學 S07）的控制項與屬性，以程式碼建立（代替設計工具產生的 Form1.Designer.cs）
public class Form1 : Form
{
    private Label label1 = new Label();
    private ListBox lstNames = new ListBox();
    private TextBox txtName = new TextBox();
    private Button btnAdd = new Button();
    private Button button1 = new Button();

    public Form1()
    {
        label1.Location = new Point(12, 9);
        label1.Text = "Names";
        lstNames.Location = new Point(12, 27);
        lstNames.Size = new Size(120, 94);
        txtName.Location = new Point(138, 26);
        txtName.Size = new Size(100, 23);
        btnAdd.Location = new Point(138, 55);
        btnAdd.Size = new Size(100, 23);
        btnAdd.Text = "Add Name";
        btnAdd.Click += btnAdd_Click;
        Text = "Names";
        Size = new Size(268, 180);
        Controls.AddRange(new Control[] { label1, lstNames, txtName, btnAdd });
    }

    // 簡報第 15 頁：設計工具產生的空白處理常式（S05）
    private void button1_Click(object sender, System.EventArgs e)
    {

    }

    // 簡報第 16 頁：官方教學的按鈕事件（S07）
    private void btnAdd_Click(object sender, EventArgs e)
    {
        if (!string.IsNullOrWhiteSpace(txtName.Text) && !lstNames.Items.Contains(txtName.Text))
            lstNames.Items.Add(txtName.Text);
    }
}
