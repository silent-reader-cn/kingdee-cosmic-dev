# 检查项生效状态-xkcts_inspectitemstatus

## 检查项生效状态-主表 t_xkinsp_itemstatus

- **表名称：** 检查项生效状态-主表
- **表名：** t_xkinsp_itemstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedataid | 基础资料 | varchar | 50 |  | √ | ' ' | 基础资料 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | feffective | 生效状态 | varchar | 1 |  | √ | '0' | 生效状态 |
| 5 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | [巡检检查项 xkcts_inspectitem](../cts_files/xkcts_inspectitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_itemstatus |  | fid |
| 2 | idx_xkinsp_itemstatus |  | fitemid |
