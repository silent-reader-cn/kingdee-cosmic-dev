# 合同类型-conm_type

## 合同类型-主表 t_conm_type

- **表名称：** 合同类型-主表
- **表名：** t_conm_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同类型分组 conm_typegroup](../conm_files/conm_typegroup.md) |
| 3 | fautovalid | 合同自动生效 | bpchar | 1 |  | √ | '0' | 合同自动生效 |
| 4 | fexcutecontrol | 合同控制 | varchar | 5 |  | √ | ' ' | 合同控制,枚举: MON :总金额 NUM :数量 PRI :单价 M&N :总金额、数量 M&P :总金额、单价 M&N&P :总金额、数量、单价 NAN :不控制 |
| 5 | fcontexecute | 执行控制 | varchar | 5 |  | √ | ' ' | 执行控制,枚举: 1 :是 0 :否 |
| 6 | fschemeid | 履行登记方案 | int8 | 64 |  | √ | 0 | [履行登记方案 conm_recordscheme](../conm_files/conm_recordscheme.md) |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcontcategoryid | 合同种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 10 | fautoending | 合同自动失效 | bpchar | 1 |  | √ | '0' | 合同自动失效 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fpaydirect | 收付方向 | varchar | 5 |  | √ | ' ' | 收付方向,枚举: REC :收 PAY :付 NAN :无 RP :收付 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | factivearchive | 启用合同归档 | bpchar | 1 |  | √ | '0' | 启用合同归档 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fconmprop | 合同属性 | varchar | 5 |  | √ | ' ' | 合同属性,枚举: A :框架协议 B :合同 |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fcategory | 合同性质（废弃） | varchar | 5 |  | √ | ' ' | 合同性质（废弃）,枚举: PUR :采购 SAL :销售 REC :收入 PAY :支出 NAN :其他 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | factivesign | 启用合同签章 | bpchar | 1 |  | √ | '0' | 启用合同签章 |
| 23 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 25 | fisexecute | 可执行 | bpchar | 1 |  | √ | '0' | 可执行 |
| 26 | fenablearchive | 启用归档申请 | bpchar | 1 |  | √ | '0' | 启用归档申请 |
| 27 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 28 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | factivereview | 启用合同评审 | bpchar | 1 |  | √ | '0' | 启用合同评审 |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_conm_type_pkey |  | fid |
| 2 | idx_conm_type_number |  | fnumber |

---

## 合同类型-多语言表 t_conm_type_l

- **表名称：** 合同类型-多语言表
- **表名：** t_conm_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_type_l_fname |  | fname,fid |
| 2 | t_conm_type_l_pkey |  | fpkid |
| 3 | idx_conm_type_l_fid |  | fid,flocaleid |
