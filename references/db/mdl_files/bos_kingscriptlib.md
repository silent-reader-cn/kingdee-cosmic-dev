# 脚本代码库-bos_kingscriptlib

## 脚本代码库-多语言表 t_bas_kingscriptlib_l

- **表名称：** 脚本代码库-多语言表
- **表名：** t_bas_kingscriptlib_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 代码提示 | varchar | 200 |  | √ | ' ' | 代码提示 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_kingscriptlib_l |  | fpkid |
| 2 | idx_bas_kingscriptlib_l_id |  | fid,flocaleid |

---

## 脚本代码库-主表 t_bas_kingscriptlib

- **表名称：** 脚本代码库-主表
- **表名：** t_bas_kingscriptlib

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcomment | 代码提示 | varchar | 200 |  | √ | ' ' | 代码提示 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fscripttype | 脚本类型 | varchar | 50 |  | √ | '1' | 脚本类型,枚举: 1 :表单插件 2 :单据插件 3 :列表插件 4 :操作插件 |
| 9 | fcode | 代码 | text | 0 |  |  | null | 代码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_kingscriptlib |  | fid |
| 2 | idx_bas_kingscriptlib_number |  | fnumber |
