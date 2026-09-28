# 高级设置基础资料-bd_advancesetting

## 高级设置基础资料-主表 t_bas_advancesetting

- **表名称：** 高级设置基础资料-主表
- **表名：** t_bas_advancesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faotuaddentry | 列表无下一焦点可切换时，自动增行 | bpchar | 1 |  | √ | ' ' | 列表无下一焦点可切换时，自动增行 |
| 3 | fautotonext | 下拉选择后自动切换下一个输入框 | bpchar | 1 |  | √ | ' ' | 下拉选择后自动切换下一个输入框 |
| 4 | fnextfieldinentry | 列表回车切换下一行输入框 | bpchar | 1 |  | √ | ' ' | 列表回车切换下一行输入框 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fnextfield | 回车切换下一个输入框 | bpchar | 1 |  | √ | ' ' | 回车切换下一个输入框 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_advancesetting |  | fid |
| 2 | idx_bas_advancesetting |  | fnextfield |
