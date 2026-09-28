# 汇总方案变更单-tctb_xorg_group

## 汇总方案变更单-主表 t_tctb_xorg_group

- **表名称：** 汇总方案变更单-主表
- **表名：** t_tctb_xorg_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | finvaliddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 4 | fprelevyrate | 预征率计算 | varchar | 50 |  | √ | ' ' | 预征率计算,枚举: 1 :固定比例 2 :累计销售额比例 3 :二级机构分配比例 |
| 5 | fsourcebillentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 6 | fparticipation | 总机构参与三因素分配 | bpchar | 1 |  | √ | '0' | 总机构参与三因素分配 |
| 7 | fblwccl | 比例尾差处理 | varchar | 50 |  | √ | ' ' | 比例尾差处理,枚举: 0 :分配至总机构 1 :分配至最大比例的组织 |
| 8 | fzfjgsefpfs | 总分机构税额分配方式 | varchar | 50 |  | √ | ' ' | 总分机构税额分配方式,枚举: 1 :按销售收入比例分配 2 :按固定比例分配 3 :按组织直接确定税额 4 :按总机构固定比例、分支机构销售收入比例分配 |
| 9 | feffectdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 1 :保存 2 :启用 3 :禁用 |
| 13 | ffixedratio | 固定比例值 | numeric | 23 | 10 | √ | 0 | 固定比例值 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fzjggdbl | 总机构固定比例（%） | numeric | 23 | 10 | √ | 0 | 总机构固定比例（%） |
| 17 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 18 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 19 | fybtsehffs | 应补退税额划分方式 | varchar | 50 |  | √ | ' ' | 应补退税额划分方式,枚举: 1 :按收入类型计算 2 :按组织分别计算 |
| 20 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :所得税 xfs :消费税 sljsjj :地方水利建设基金 cwbb :财务报表 |
| 21 | ffpxssrfw | 分配销售收入范围 | varchar | 50 |  | √ | ' ' | 分配销售收入范围,枚举: 1 :全部销售收入 2 :自动判断收入范围 |
| 22 | fsourcebillno | 汇总方案编码 | varchar | 100 |  | √ | ' ' | 汇总方案编码 |
| 23 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fsourcebillstatus | 汇总方案单据状态 | varchar | 50 |  | √ | ' ' | 汇总方案单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 29 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 30 | fsummaryorgtype | 汇总企业类型 | varchar | 50 |  | √ | ' ' | 汇总企业类型,枚举: 1 :航空运输企业 2 :铁路运输企业 3 :邮政企业 4 :电信企业 5 :一般企业 |
| 31 | fvalidstatus | 生效状态 | varchar | 50 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 32 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | fsummaryway | 汇总方式 | varchar | 50 |  | √ | ' ' | 汇总方式,枚举: 1 :预征方式 2 :分配方式 3 :仅汇总，不分配不预征 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_xorg_group |  | fid |
| 2 | idx_tctb_xorgg_sourid |  | fsourcebillid |

---

## 汇总组织-子表 t_tctb_xorggroup_detail

- **表名称：** 汇总组织-子表
- **表名：** t_tctb_xorggroup_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fentrysrcid | 源分录行ID | int8 | 64 |  | √ | 0 | 源分录行ID |
| 4 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | parententryid | parententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | forgcode | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 7 | forgid | 组织id | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fkdqjyqylx | 跨地区经营企业类型 | varchar | 50 |  | √ | ' ' | 跨地区经营企业类型,枚举: 100 :非跨地区经营企业 210 :总机构（跨省）——适用《跨地区经营汇总纳税企业所得税征收管理办法》 220 :总机构（跨省）——不适用《跨地区经营汇总纳税企业所得税征收管理办法》 230 :总机构（省内） 311 :分支机构（须进行完整年度申报并按比例纳税） 312 :分支机构（须进行完整年度申报但不就地缴纳） |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fissuesbb | 出具申报表 | bpchar | 1 |  | √ | '0' | 出具申报表 |
| 11 | fdeclaration | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 12 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 13 | fcollectorg | 文本 | varchar | 50 |  | √ | ' ' | 文本 |
| 14 | forgname | 组织名称 | varchar | 50 |  | √ | ' ' | 组织名称 |
| 15 | fshareid | 分摊标识 | bpchar | 1 |  | √ | '0' | 分摊标识 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrychangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 18 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_xorggroup_detail |  | fentryid |
| 2 | idx_tctb_xorgg_detail_fk |  | fid |

---

## 分配参数-子表 t_tctb_xorggroup_param

- **表名称：** 分配参数-子表
- **表名：** t_tctb_xorggroup_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysrcid | 源分录行ID | int8 | 64 |  | √ | 0 | 源分录行ID |
| 3 | fdeclare | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 4 | fjzjtysbl | 即征即退应税服务分配比例 | numeric | 23 | 10 | √ | 0 | 即征即退应税服务分配比例 |
| 5 | fybxmhwbl | 一般项目货物及劳务分配比例 | numeric | 23 | 10 | √ | 0 | 一般项目货物及劳务分配比例 |
| 6 | fjzjthwbl | 即征即退货物及劳务分配比例 | numeric | 23 | 10 | √ | 0 | 即征即退货物及劳务分配比例 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fybxmysbl | 一般项目应税服务分配比例 | numeric | 23 | 10 | √ | 0 | 一般项目应税服务分配比例 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fentrychangetype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :修改 C :删除 |
| 11 | forg | 组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_xorgg_param_fk |  | fid |
| 2 | pk_tctb_xorggroup_param |  | fentryid |

---

## 汇总方案变更单-多语言表 t_tctb_xorg_group_l

- **表名称：** 汇总方案变更单-多语言表
- **表名：** t_tctb_xorg_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 汇总方案名称 | varchar | 50 |  | √ | ' ' | 汇总方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_xorg_group_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_xorg_group_l |  | fpkid |
