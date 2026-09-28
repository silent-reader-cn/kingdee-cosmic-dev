# 工作台待办页签状态-pbd_todostatus

## 工作台待办页签状态-多语言表 t_pbd_todostatus_l

- **表名称：** 工作台待办页签状态-多语言表
- **表名：** t_pbd_todostatus_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 状态名称 | varchar | 255 |  | √ | ' ' | 状态名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_todostatus_l_fid |  | fid |
| 2 | pk_pbd_todostatus_l |  | fpkid |

---

## 工作台待办页签状态-主表 t_pbd_todostatus

- **表名称：** 工作台待办页签状态-主表
- **表名：** t_pbd_todostatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 状态名称 | varchar | 20 |  | √ | ' ' | 状态名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fnumber | 状态编码 | varchar | 80 |  | √ | ' ' | 状态编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_todo_status_fmasterid |  | fmasterid |
| 2 | pk_pbd_todostatus |  | fid |
| 3 | idx_pbd_todo_status_fnumber |  | fnumber |
