# 集团名册-tcvvt_group_book

## 集团组织-子表 t_tcvvt_group_org

- **表名称：** 集团组织-子表
- **表名：** t_tcvvt_group_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgcode | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 3 | fleverno | fleverno | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fregistertypeid | fregistertypeid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fcreditcode | fcreditcode | varchar | 50 |  | √ | ' ' |  |
| 9 | fstockno | fstockno | varchar | 50 |  | √ | ' ' |  |
| 10 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 11 | flocaltaxsn | flocaltaxsn | varchar | 50 |  | √ | ' ' |  |
| 12 | fsuperorgname | fsuperorgname | varchar | 100 |  | √ | ' ' |  |
| 13 | ftrade | ftrade | varchar | 50 |  | √ | ' ' |  |
| 14 | flocaltaxorg | flocaltaxorg | varchar | 50 |  | √ | ' ' |  |
| 15 | fnationtaxorg | fnationtaxorg | varchar | 50 |  | √ | ' ' |  |
| 16 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 18 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | felectronicfileno | felectronicfileno | varchar | 50 |  | √ | ' ' |  |
| 20 | fisvirtualnode | fisvirtualnode | varchar | 30 |  | √ | ' ' |  |
| 21 | fadress | fadress | varchar | 50 |  | √ | ' ' |  |
| 22 | parententryid | parententryid | int8 | 64 |  | √ | 0 | pid |
| 23 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 24 | fispointcompany | fispointcompany | varchar | 30 |  | √ | ' ' |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | ftaxername | ftaxername | varchar | 100 |  | √ | ' ' |  |
| 27 | fcommiterphone | fcommiterphone | varchar | 50 |  | √ | ' ' |  |
| 28 | fnationtaxsn | fnationtaxsn | varchar | 50 |  | √ | ' ' |  |
| 29 | fcommitername | fcommitername | varchar | 50 |  | √ | ' ' |  |
| 30 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 31 | fispubliccompany | fispubliccompany | varchar | 30 |  | √ | ' ' |  |
| 32 | faccountway | faccountway | varchar | 50 |  | √ | ' ' |  |
| 33 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 34 | fcodeandnameid | fcodeandnameid | int8 | 64 |  | √ | 0 |  |
| 35 | frollstatus | frollstatus | varchar | 30 |  | √ | ' ' |  |
| 36 | fgrouproll | fgrouproll | varchar | 100 |  | √ | ' ' |  |
| 37 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 38 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 39 | fisvalid | fisvalid | varchar | 30 |  | √ | ' ' |  |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fisabroad | fisabroad | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_group_org_fk |  | fid |
| 2 | pk_t_tcvvt_group_org |  | fentryid |

---

## 集团名册-主表 t_tcvvt_group_book

- **表名称：** 集团名册-主表
- **表名：** t_tcvvt_group_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: 1 :保存 2 :启用 3 :禁用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fenddate | 有效起止 | timestamp | 0 |  |  | null | 有效起止 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 9 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 集团编码 | varchar | 30 |  | √ | ' ' | 集团编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_group_book |  | fid |
| 2 | idx_tcvvt_group_book |  | fnumber |

---

## 集团名册-多语言表 t_tcvvt_group_book_l

- **表名称：** 集团名册-多语言表
- **表名：** t_tcvvt_group_book_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 集团方案 | varchar | 200 |  | √ | ' ' | 集团方案 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_group_book_l_0 |  | fid,flocaleid |
| 2 | pk_tcvvt_group_book_l |  | fpkid |
