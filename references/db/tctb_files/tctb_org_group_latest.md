# 汇总方案-tctb_org_group_latest

## 汇总组织-子表 t_tctb_org_group_detail

- **表名称：** 汇总组织-子表
- **表名：** t_tctb_org_group_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgcode | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |
| 5 | parententryid | parententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fkdqjyqylx | 跨地区经营企业类型 | varchar | 50 |  | √ | ' ' | 跨地区经营企业类型,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fissuesbb | 出具申报表 | bpchar | 1 |  | √ | ' ' | 出具申报表 |
| 10 | fdeclaration | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 11 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 12 | fcollectorg | 文本 | varchar | 100 |  |  | ' ' | 文本 |
| 13 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 14 | fshareid | 分摊标识 | bpchar | 1 |  | √ | ' ' | 分摊标识 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fentrychangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 17 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 |

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

## 汇总方案-主表 t_tctb_org_group

- **表名称：** 汇总方案-主表
- **表名：** t_tctb_org_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fprelevyrate | 预征率计算 | varchar | 50 |  | √ | ' ' | 预征率计算,枚举: 1 :固定比例 2 :累计销售额比例 3 :二级机构分配比例 |
| 4 | fparticipation | 总机构参与三因素分配 | bpchar | 1 |  | √ | '0' | 总机构参与三因素分配 |
| 5 | fblwccl | 比例尾差处理 | varchar | 50 |  | √ | ' ' | 比例尾差处理,枚举: 0 :分配至总机构 1 :分配至最大比例的组织 |
| 6 | fzfjgsefpfs | 总分机构税额分配方式 | varchar | 50 |  | √ | ' ' | 总分机构税额分配方式,枚举: 1 :按销售收入比例分配 2 :按固定比例分配 3 :按组织直接确定税额 4 :按总机构固定比例、分支机构销售收入比例分配 |
| 7 | feffectdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: 1 :保存 2 :启用 3 :禁用 |
| 11 | ffixedratio | 固定比例值 | numeric | 23 | 10 | √ | 0 | 固定比例值 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsummarypurpose | 汇总用途 | varchar | 50 |  | √ | ' ' | 汇总用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 15 | fzjggdbl | 总机构固定比例（%） | numeric | 23 | 10 | √ | 0 | 总机构固定比例（%） |
| 16 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 17 | fybtsehffs | 应补退税额划分方式 | varchar | 50 |  | √ | ' ' | 应补退税额划分方式,枚举: 1 :按收入类型计算 2 :按组织分别计算 |
| 18 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :所得税 xfs :消费税 sljsjj :地方水利建设基金 cwbb :财务报表 |
| 19 | ffpxssrfw | 分配销售收入范围 | varchar | 50 |  | √ | ' ' | 分配销售收入范围,枚举: 1 :全部销售收入 2 :自动判断收入范围 |
| 20 | fxfszfjgsefpfs | 总分机构税额分配方式 | varchar | 50 |  | √ | ' ' | 总分机构税额分配方式,枚举: 2 :按固定比例分配 |
| 21 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 22 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fstepsummary | 逐级汇总 | bpchar | 1 |  | √ | '0' | 逐级汇总 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fybtsejsfs | 应补退税额计算方式 | varchar | 50 |  | √ | ' ' | 应补退税额计算方式,枚举: 1 :按销售收入比例划分 2 :按销项税额比例划分 |
| 28 | fsummaryorgtype | 汇总企业类型 | varchar | 30 |  | √ | ' ' | 汇总企业类型,枚举: 1 :航空运输企业 2 :铁路运输企业 3 :邮政企业 4 :电信企业 5 :一般企业 |
| 29 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 方案编码 | varchar | 100 |  | √ | ' ' | 方案编码 |
| 32 | fsummarydeclaration | 税局汇总申报 | bpchar | 1 |  | √ | '0' | 税局汇总申报 |
| 33 | fsummaryway | 汇总方式 | varchar | 30 |  | √ | ' ' | 汇总方式,枚举: 1 :预征方式 2 :分配方式 3 :仅汇总，不分配不预征 |

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

## 消费税分配参数-子表 t_tctb_orggroup_xfsparam

- **表名称：** 消费税分配参数-子表
- **表名：** t_tctb_orggroup_xfsparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fxfsbl | 比例 | numeric | 23 | 10 | √ | 0 | 比例 |
| 3 | fxfsorg | 消费税组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fentrychangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 7 | fxfsdeclare | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orggroup_xfsparam |  | fid |
| 2 | pk_tctb_orggroup_xfsparam |  | fentryid |

---

## 分配参数-子表 t_tctb_org_group_param

- **表名称：** 分配参数-子表
- **表名：** t_tctb_org_group_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeclare | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 3 | fjzjtysbl | 即征即退应税服务分配比例 | numeric | 23 | 10 | √ | 0 | 即征即退应税服务分配比例 |
| 4 | fybxmhwbl | 一般项目货物及劳务分配比例 | numeric | 23 | 10 | √ | 0 | 一般项目货物及劳务分配比例 |
| 5 | fjzjthwbl | 即征即退货物及劳务分配比例 | numeric | 23 | 10 | √ | 0 | 即征即退货物及劳务分配比例 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fybxmysbl | 一般项目应税服务分配比例 | numeric | 23 | 10 | √ | 0 | 一般项目应税服务分配比例 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrychangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 10 | forg | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tctb_org_group_param |  | fentryid |
| 2 | index_tctb_org_group_param |  | fid |

---

## 汇总方案-多语言表 t_tctb_org_group_l

- **表名称：** 汇总方案-多语言表
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

---

## 汇总维度-多语言表 t_tctb_org_group_dim_l

- **表名称：** 汇总维度-多语言表
- **表名：** t_tctb_org_group_dim_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimvaluename | 维度值 | varchar | 200 |  | √ | ' ' | 维度值 |
| 2 | fdimremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_org_group_dim_l |  | fpkid |
| 2 | idx_tctb_org_group_dim_l_0 |  | fdetailid,flocaleid |

---

## 汇总维度-子表 t_tctb_org_group_dim

- **表名称：** 汇总维度-子表
- **表名：** t_tctb_org_group_dim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentrychangetype2 | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 2 | fdimvalueid | 维度值ID | varchar | 100 |  | √ | ' ' | 维度值ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdimvaluename | 维度值 | varchar | 200 |  | √ | ' ' | 维度值 |
| 5 | fdimremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 6 | fdimlevel | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 |
| 7 | fdimparentid | 上级维度 | varchar | 50 |  | √ | ' ' | 上级维度 |
| 8 | fdimtype | 维度 | varchar | 50 |  | √ | ' ' | 维度,枚举: bos_org :核算组织 tctb_orgmapentity :业务维度 |
| 9 | fparentdetailid | fparentdetailid | int8 | 64 |  | √ | 0 | pid |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fdimclass | 组织映射方案ID | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fdimvaluenumber | 维度值编码 | varchar | 100 |  | √ | ' ' | 维度值编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_org_group_dim |  | fdetailid |
| 2 | idx_t_tctb_org_group_dim |  | fentryid |
