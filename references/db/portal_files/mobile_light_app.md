# 星瀚应用-mobile_light_app

## 星瀚应用-主表 t_bas_mobile_app

- **表名称：** 星瀚应用-主表
- **表名：** t_bas_mobile_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ficonurl | 图标 | varchar | 250 |  | √ | ' ' | 图标 |
| 3 | fappname | 星瀚应用名称 | varchar | 150 |  | √ | ' ' | 星瀚应用名称 |
| 4 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 5 | fformtype | 表单类型 | bpchar | 1 |  | √ | '1' | 表单类型,枚举: 1 :表单页面 2 :轻分析 |
| 6 | fformnum | 表单编码 | varchar | 150 |  | √ | ' ' | 表单编码 |
| 7 | fappnum | 表单应用编码 | varchar | 36 |  | √ | ' ' | 表单应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_mobile_app |  | fid |
| 2 | idx_app_mob_form |  | fformnum |

---

## 星瀚应用-多语言表 t_bas_mobile_app_l

- **表名称：** 星瀚应用-多语言表
- **表名：** t_bas_mobile_app_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappname | 星瀚应用名称 | varchar | 150 |  | √ | ' ' | 星瀚应用名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_mobile_app_l |  | fpkid |
| 2 | idx_bas_mobile_app_l_0 |  | fid,flocaleid |
