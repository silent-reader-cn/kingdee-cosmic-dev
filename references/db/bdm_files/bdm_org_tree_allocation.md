# 分配组织树形列表-bdm_org_tree_allocation

## 分配组织树形列表-多语言表 t_bdm_org_l

- **表名称：** 分配组织树形列表-多语言表
- **表名：** t_bdm_org_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftreename | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 4 | ffullname | 长名称 | varchar | 200 |  | √ | ' ' | 长名称 |
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

## 分配组织树形列表-主表 t_bdm_org

- **表名称：** 分配组织树形列表-主表
- **表名：** t_bdm_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenterprisemainorg | fenterprisemainorg | varchar | 10 |  | √ | '0' |  |
| 3 | fisleaf | 是否叶子 | varchar | 10 |  | √ | '0' | 是否叶子 |
| 4 | fqrcodestatus | fqrcodestatus | varchar | 10 |  | √ | ' ' |  |
| 5 | fdefaultdev | fdefaultdev | varchar | 50 |  | √ | ' ' |  |
| 6 | fparentname | fparentname | varchar | 200 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fepinfo | fepinfo | int8 | 64 |  | √ | 0 |  |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | falleaccount | falleaccount | int8 | 64 |  | √ | 0 |  |
| 13 | fviewtype | fviewtype | varchar | 50 |  | √ | ' ' |  |
| 14 | fname | 基础资料name | varchar | 200 |  | √ | ' ' | 基础资料name |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdefaultterminal | fdefaultterminal | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 19 | fparentbase | 上级 | int8 | 64 |  | √ | 0 | [分配组织树形列表 bdm_org_tree_allocation](../bdm_files/bdm_org_tree_allocation.md) |
| 20 | fequipmenttype | fequipmenttype | varchar | 60 |  | √ | ' ' |  |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
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
