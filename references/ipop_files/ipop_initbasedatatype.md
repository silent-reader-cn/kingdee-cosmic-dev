# 基础资料录入类型（废弃）-ipop_initbasedatatype

## 基础资料录入类型（废弃）-主表 t_ipop_initbasedatatype

- **表名称：** 基础资料录入类型（废弃）-主表
- **表名：** t_ipop_initbasedatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodulename | 模块名称 | varchar | 255 |  | √ | ' ' | 模块名称 |
| 3 | fappnumber | 应用简码 | varchar | 50 |  | √ | ' ' | 应用简码 |
| 4 | fmodulecode | 模块编码 | varchar | 50 |  | √ | ' ' | 模块编码 |
| 5 | fmenuappnum | 菜单应用简码 | varchar | 50 |  | √ | ' ' | 菜单应用简码 |
| 6 | fformid | 资料标识 | varchar | 50 |  | √ | ' ' | 资料标识 |
| 7 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |
| 8 | fmenuid | 菜单id | varchar | 50 |  | √ | ' ' | 菜单id |
| 9 | fisorg | 复选框 | bpchar | 1 |  | √ | ' ' | 复选框 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_initbasedatatype_fmid |  | fformid |
| 2 | idx_ipop_initbasedatatype_app |  | fappnumber |
| 3 | idx_ipop_initbasedatatype_mod |  | fmodulecode |
| 4 | pk_t_ipop_initbasedatatype |  | fid |

---

## 基础资料录入类型（废弃）-多语言表 t_ipop_initbasedatatype_l

- **表名称：** 基础资料录入类型（废弃）-多语言表
- **表名：** t_ipop_initbasedatatype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodulename | 模块名称 | varchar | 255 |  | √ | ' ' | 模块名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_initbasedatatype_l |  | fpkid |
| 2 | idx_ipop_initbasedatatype_l |  | fid,flocaleid |
