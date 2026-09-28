# 跨境交易字段-bei_crosstranfield

## 跨境交易字段-多语言表 t_bei_crosstranfield_l

- **表名称：** 跨境交易字段-多语言表
- **表名：** t_bei_crosstranfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fcomboxvalue | 枚举值 | varchar | 500 |  | √ | ' ' | 枚举值 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_crosstranfield_l_pkey |  | fpkid |
| 2 | idx_bei_crosstranfield_l |  | fid,fname,fcomment |

---

## 跨境交易字段-主表 t_bei_crosstranfield

- **表名称：** 跨境交易字段-主表
- **表名：** t_bei_crosstranfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fisnotnull | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 5 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fissee | 可见 | bpchar | 1 |  | √ | '0' | 可见 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcomboxvalue | 枚举值 | varchar | 500 |  | √ | ' ' | 枚举值 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: text :文本 date :日期 f7 :F7 combox :下拉框 bool :布尔 |
| 17 | fbasedatatype | 基础资料类型 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_crosstranfield_pkey |  | fid |
| 2 | idx_bei_crosstranfield |  | fenable |
