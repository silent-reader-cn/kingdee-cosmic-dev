# 非组织树企业-bdm_org_nottree_list

## 非组织树企业-多语言表 t_bdm_org_l

- **表名称：** 非组织树企业-多语言表
- **表名：** t_bdm_org_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftreename | ftreename | varchar | 200 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | ffullname | ffullname | varchar | 200 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_org_l_0 |  | fid,flocaleid |
| 2 | pk_bdm_org_l |  | fpkid |

---

## 非组织树企业-主表 t_bdm_org

- **表名称：** 非组织树企业-主表
- **表名：** t_bdm_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenterprisemainorg | 企业主体组织 | varchar | 10 |  | √ | '0' | 企业主体组织,枚举: 0 :否 1 :是 |
| 3 | fisleaf | fisleaf | varchar | 10 |  | √ | '0' |  |
| 4 | fqrcodestatus | fqrcodestatus | varchar | 10 |  | √ | ' ' |  |
| 5 | fdefaultdev | fdefaultdev | varchar | 50 |  | √ | ' ' |  |
| 6 | fparentname | 上级组织名称 | varchar | 200 |  | √ | ' ' | 上级组织名称 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | falleaccount | falleaccount | int8 | 64 |  | √ | 0 |  |
| 13 | fviewtype | fviewtype | varchar | 50 |  | √ | ' ' |  |
| 14 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdefaultterminal | fdefaultterminal | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | flongnumber | flongnumber | varchar | 200 |  | √ | ' ' |  |
| 19 | fparentbase | fparentbase | int8 | 64 |  | √ | 0 |  |
| 20 | fequipmenttype | fequipmenttype | varchar | 60 |  | √ | ' ' |  |
| 21 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 22 | fdevlist_tag | fdevlist_tag | text | 0 |  |  | null |  |
| 23 | fparent | 上级组织id | varchar | 200 |  | √ | ' ' | 上级组织id |
| 24 | fissuetype | fissuetype | varchar | 60 |  | √ | ' ' |  |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 27 | fdevlist | fdevlist | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_org |  | fid |
| 2 | idx_bdm_org |  | fnumber |
