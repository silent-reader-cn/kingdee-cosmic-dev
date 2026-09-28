# 脚本模板-bos_scripttemplate

## 脚本模板-主表 t_bas_scripttemplate

- **表名称：** 脚本模板-主表
- **表名：** t_bas_scripttemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 256 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fscriptcontent_tag | 脚本_详情 | text | 0 |  |  | null | 脚本_详情 |
| 6 | fsource | fsource | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftype | 模板类型 | varchar | 30 |  | √ | ' ' | 模板类型,枚举: ZPL :ZPL EPL :EPL |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |
| 14 | fscriptcontent | 脚本 | varchar | 255 |  | √ | ' ' | 脚本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_scripttemplate |  | fid |
| 2 | idx_bas_scripttemplate_n |  | fnumber |

---

## 脚本模板-多语言表 t_bas_scripttemplate_l

- **表名称：** 脚本模板-多语言表
- **表名：** t_bas_scripttemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 256 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_scripttemplate_l |  | fpkid |
| 2 | idx_bas_scripttemplate_l |  | fid,flocaleid |
