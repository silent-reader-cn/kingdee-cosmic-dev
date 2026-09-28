# 增值税汇总方案-t_org_group

## 单据体-子表 t_tctb_org_group_detail

- **表名称：** 单据体-子表
- **表名：** t_tctb_org_group_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [税务组织实体 tctb_org_entity](../tctb_files/tctb_org_entity.md) |
| 4 | forgcode | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |
| 5 | parententryid | parententryid | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fkdqjyqylx | fkdqjyqylx | varchar | 50 |  | √ | ' ' |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fissuesbb | fissuesbb | bpchar | 1 |  | √ | ' ' |  |
| 10 | fdeclaration | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 11 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 12 | fcollectorg | fcollectorg | varchar | 100 |  |  | ' ' |  |
| 13 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 14 | fshareid | fshareid | bpchar | 1 |  | √ | ' ' |  |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fentrychangetype | fentrychangetype | varchar | 50 |  | √ | ' ' |  |
| 17 | flevelname | flevelname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_org_group_detail_pkey |  | fentryid |
| 2 | idx_t_tctb_org_group_detail |  | fid |

---

## 增值税汇总方案-主表 t_tctb_org_group

- **表名称：** 增值税汇总方案-主表
- **表名：** t_tctb_org_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fprelevyrate | fprelevyrate | varchar | 50 |  | √ | ' ' |  |
| 4 | fparticipation | fparticipation | bpchar | 1 |  | √ | '0' |  |
| 5 | fblwccl | fblwccl | varchar | 50 |  | √ | ' ' |  |
| 6 | fzfjgsefpfs | fzfjgsefpfs | varchar | 50 |  | √ | ' ' |  |
| 7 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchangestatus | fchangestatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | ffixedratio | ffixedratio | numeric | 23 | 10 | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsummarypurpose | fsummarypurpose | varchar | 50 |  | √ | ' ' |  |
| 15 | fzjggdbl | fzjggdbl | numeric | 23 | 10 | √ | 0 |  |
| 16 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 17 | fybtsehffs | fybtsehffs | varchar | 50 |  | √ | ' ' |  |
| 18 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 19 | ffpxssrfw | ffpxssrfw | varchar | 50 |  | √ | ' ' |  |
| 20 | fxfszfjgsefpfs | fxfszfjgsefpfs | varchar | 50 |  | √ | ' ' |  |
| 21 | fversion | fversion | varchar | 30 |  | √ | ' ' |  |
| 22 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 25 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fybtsejsfs | fybtsejsfs | varchar | 50 |  | √ | ' ' |  |
| 28 | fsummaryorgtype | fsummaryorgtype | varchar | 30 |  | √ | ' ' |  |
| 29 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 方案编码 | varchar | 100 |  | √ | ' ' | 方案编码 |
| 32 | fsummarydeclaration | fsummarydeclaration | bpchar | 1 |  | √ | '0' |  |
| 33 | fsummaryway | fsummaryway | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_org_group |  | fnumber |
| 2 | t_tctb_org_group_pkey |  | fid |

---

## 增值税汇总方案-多语言表 t_tctb_org_group_l

- **表名称：** 增值税汇总方案-多语言表
- **表名：** t_tctb_org_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_org_group_l |  | fid |
| 2 | t_tctb_org_group_l_pkey |  | fpkid |
