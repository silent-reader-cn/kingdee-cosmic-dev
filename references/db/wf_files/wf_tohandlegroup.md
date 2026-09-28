# 待办分组-wf_tohandlegroup

## 待办分组-多语言表 t_wf_tohandlegroup_l

- **表名称：** 待办分组-多语言表
- **表名：** t_wf_tohandlegroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 待办分组 | varchar | 500 |  | √ | ' ' | 待办分组 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_tohandlegroup_l_pkey |  | fpkid |
| 2 | idx_wf_tohandlegroup_l |  | fid,flocaleid |

---

## 待办分组-主表 t_wf_tohandlegroup

- **表名称：** 待办分组-主表
- **表名：** t_wf_tohandlegroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frule | 分组规则 | varchar | 500 |  | √ | ' ' | 分组规则 |
| 3 | fname | 待办分组 | varchar | 500 |  | √ | ' ' | 待办分组 |
| 4 | fnumber | 编码 | int8 | 64 |  | √ | 0 | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_tohandlegroup_pkey |  | fid |
| 2 | idx_wf_tohandlegroup_number |  | fnumber |
