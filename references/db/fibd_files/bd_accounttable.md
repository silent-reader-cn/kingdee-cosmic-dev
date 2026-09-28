# 科目表-bd_accounttable

## 科目表-主表 t_bd_accounttable

- **表名称：** 科目表-主表
- **表名：** t_bd_accounttable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmaxlevel | 最大级次 | int8 | 64 |  | √ | 0 | 最大级次 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fisextendpnum | 校验下级科目编码 | bpchar | 1 |  | √ | '1' | 校验下级科目编码 |
| 7 | fseperator | 分隔符 | bpchar | 1 |  | √ | ' ' | 分隔符,枚举: : . :. |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fisuseseperator | fisuseseperator | bpchar | 1 |  | √ | '0' |  |
| 11 | fisuserlevel | fisuserlevel | bpchar | 1 |  | √ | '0' |  |
| 12 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | felementid | 会计要素表 | int8 | 64 |  | √ | 0 | 会计要素表 bd_element_table |
| 14 | fisinternational | 启用国际会计准则 | bpchar | 1 |  | √ | '0' | 启用国际会计准则 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | faccountlevel | 科目级次 | varchar | 50 |  | √ | ' ' | 科目级次 |
| 17 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_acttab_num |  | fnumber |
| 2 | t_bd_accounttable_pkey |  | fid |

---

## 科目表-多语言表 t_bd_accounttable_l

- **表名称：** 科目表-多语言表
- **表名：** t_bd_accounttable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accounttable_l_pkey |  | fpkid |
| 2 | idx_bd_acttab_l_fid |  | fid,flocaleid |
