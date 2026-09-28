# 银行类别-bd_bankcgsetting

## 银行类别-多语言表 t_bd_bankcgsetting_l

- **表名称：** 银行类别-多语言表
- **表名：** t_bd_bankcgsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_bankcgsetting_l |  | fpkid |
| 2 | idx_t_bd_bankcgsetting_l_fid |  | fid,flocaleid,fname |
| 3 | idx_bd_bankcgsetting_l_fid |  | fid |

---

## 银行类别-主表 t_bd_bankcgsetting

- **表名称：** 银行类别-主表
- **表名：** t_bd_bankcgsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 4 | fisleaf | fisleaf | bpchar | 1 |  | √ | '0' |  |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flongnumber | flongnumber | varchar | 100 |  | √ | ' ' |  |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fwbschemeid | 网上银行对接平台 | varchar | 50 |  | √ | ' ' | 网上银行对接平台,枚举: 0 : 1 :银企云 2 :招行CBS8 3 :宁波银行财资大管家 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 14 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fnameloc | fnameloc | varchar | 50 |  | √ | ' ' |  |
| 20 | ftypecode | 行别代码 | varchar | 50 |  | √ | ' ' | 行别代码 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fcode | 银行简码 | varchar | 50 |  | √ | ' ' | 银行简码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_bankcgsetting |  | fid |
| 2 | idx_bd_bankcgsetting_num |  | fnumber |
