# 现金流量项目表-gl_cashflowitemtb

## 现金流量项目表-多语言表 t_gl_cashflowitemtb_l

- **表名称：** 现金流量项目表-多语言表
- **表名：** t_gl_cashflowitemtb_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gl_cashflowitemtb_l |  | fpkid |
| 2 | idx_cashflowitemtb_local |  | fid,flocaleid |

---

## 现金流量项目表-主表 t_gl_cashflowitemtb

- **表名称：** 现金流量项目表-主表
- **表名：** t_gl_cashflowitemtb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | felementtableid | 会计要素表 | int8 | 64 |  | √ | 0 | [会计要素表 bd_element_table](../gl_files/bd_element_table.md) |
| 3 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 4 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_cashflowitemtb_fno |  | fnumber |
| 2 | pk_gl_cashflowitemtb |  | fid |
