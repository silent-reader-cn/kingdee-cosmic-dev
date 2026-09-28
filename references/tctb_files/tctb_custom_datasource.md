# 数据源配置-tctb_custom_datasource

## 数据源配置-主表 t_tctb_datasource

- **表名称：** 数据源配置-主表
- **表名：** t_tctb_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 适用场景 | int8 | 64 |  | √ | 0 | 自定义数据源分组 tctb_datasource_group |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgtakerelation | 组织取数关系 | bpchar | 1 |  | √ | ' ' | 组织取数关系 |
| 5 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 6 | fischild | 是否主子关系 | bpchar | 1 |  | √ | ' ' | 是否主子关系 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fentityname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsubentityname | 子实体名称 | varchar | 50 |  | √ | ' ' | 子实体名称 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fcondition | 关联条件 | varchar | 50 |  | √ | ' ' | 关联条件 |
| 18 | ftaxtype | 适用税种类型 | varchar | 500 |  | √ | ' ' | 适用税种类型,枚举: VAT_INCOME :增值税-收入取数规则 VAT_ROLLOUT :增值税-进项税额转出取数规则 VAT_DIFF :增值税-差额扣除取数规则 CSD_AQHZ :印花税-按期汇总 CSD_HDZS :印花税-核定征收 VAT_DEDUCTION :增值税-减税项目取数规则 CIT_YJ :企业所得税-预缴取数 VAT-PREPAY :增值税-预缴项目规则 CIT-ZCZJ :企业所得税-资产折旧摊销规则 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fuserorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | ftype | 表类型 | varchar | 500 |  | √ | ' ' | 表类型,枚举: 0 :自定义 1 :发票数据 2 :财务数据 3 :增值税台账 4 :增值税一般纳税人 3302 :增值税一般纳税人底稿 11 :增值税小规模申报表 17 :增值税小规模台账 3301 :增值税小规模纳税人底稿 3304 :增值税小规模小微免税月度台账 3305 :增值税小规模纳税人季度 3306 :增值税预缴税款表 3307 :增值税一般纳税人分支机构汇总申报 3308 :增值税一般纳税人总机构一般企业汇总申报 3309 :增值税一般纳税人总机构汇总申报 5 :所得税底稿 6 :所得税申报表季报 7 :所得税申报表年报 8 :所得税季报台账 12 :所得税申报表月报 14 :所得税核定征收月报 15 :所得税核定征收季报 16 :所得税核定征收年报 13 :所得税分支机构申报表年报 9 :印花税 10 :房产和城镇土地使用税 20 :附加税费 3000 :环保税 4000 :资源税 5000 :车船税 6000 :烟类消费税 6001 :卷烟批发消费税 7000 :烟叶税 8000 :财产行为税 8001 :财产行为税计税表 8002 :其他涉税数据 9000 :水资源税A 9001 :水资源税B 9200 :一般企业汇总申报预征方式总机构 9201 :一般企业汇总申报预征方式分支机构 9202 :一般企业汇总申报仅汇总 10000 :海外增值税 10001 :海外所得税 10002 :美国所得税 10003 :计提与申报比对（海外增值税） 10004 :计提与申报比对（海外所得税） 10005 :计提与申报比对（美国所得税） |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fbblx | 报表类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_datasource_master |  | fmasterid |
| 2 | pk_tctb_datasource |  | fid |
| 3 | idx_t_tctb_datasource_createorg |  | fcreateorgid |
| 4 | idx_tctb_datasource |  | fnumber,fstatus,fenable,forgid |

---

## 字段配置-子表 t_tctb_datasource_entry

- **表名称：** 字段配置-子表
- **表名：** t_tctb_datasource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccessmap | 取数映射 | int8 | 64 |  | √ | 0 | 税务组织映射方案 tctb_orgmapentity |
| 3 | fwherestate | 过滤字段 | bpchar | 1 |  | √ | ' ' | 过滤字段 |
| 4 | finspectionshowfield | 抽检展示字段 | bpchar | 1 |  | √ | ' ' | 抽检展示字段 |
| 5 | fdescrice | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 6 | fsubname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 7 | felementwhere | 抽检条件字段 | bpchar | 1 |  | √ | ' ' | 抽检条件字段 |
| 8 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 9 | faccesslogic | 取数逻辑 | varchar | 50 |  | √ | ' ' | 取数逻辑,枚举: bqhj :本期合计 bnlj :本年累计 jzqms :截至期末数 jzqcs :截至期初数 sqqms :上期期末数 snljs :上年累计数 snxqs :上年下期数 |
| 10 | fdrilldown | 下钻展示字段 | bpchar | 1 |  | √ | '0' | 下钻展示字段 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | forgstate | 组织字段 | bpchar | 1 |  | √ | ' ' | 组织字段 |
| 13 | fisamount | 金额字段 | bpchar | 1 |  | √ | ' ' | 金额字段 |
| 14 | fyearstate | 年份字段 | bpchar | 1 |  | √ | ' ' | 年份字段 |
| 15 | fmonthstate | 月份字段 | bpchar | 1 |  | √ | ' ' | 月份字段 |
| 16 | fstate | 查询状态 | bpchar | 1 |  | √ | ' ' | 查询状态 |
| 17 | fdatastate | 时间字段 | bpchar | 1 |  | √ | ' ' | 时间字段 |
| 18 | fbizsubname | 业务名称 | varchar | 500 |  | √ | ' ' | 业务名称 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_datasource_entry |  | fentryid |
| 2 | idx_tctb_datasource_entry_fk |  | fid |

---

## 适用取数规则-多选基础资料表 t_tctb_datasource_pkrules

- **表名称：** 适用取数规则-多选基础资料表
- **表名：** t_tctb_datasource_pkrules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 自定义数据源适用取数规则 tctb_datasource_peek_rule |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_datasource_pkrules_fk |  | fid |
| 2 | pk_tctb_datasource_pkrules |  | fpkid |

---

## 数据源配置-使用范围位图表 t_tctb_datasource_m

- **表名称：** 数据源配置-使用范围位图表
- **表名：** t_tctb_datasource_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tctb_datasource_m |  | forgid |

---

## 数据源配置-多语言表 t_tctb_datasource_l

- **表名称：** 数据源配置-多语言表
- **表名：** t_tctb_datasource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_datasource_l |  | fpkid |
| 2 | idx_tctb_datasource_l_0 |  | fid,flocaleid |

---

## 数据源配置-使用范围表 t_tctb_datasource_u

- **表名称：** 数据源配置-使用范围表
- **表名：** t_tctb_datasource_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tctb_datasource_u |  | fdataid,fuseorgid |
| 2 | idx_t_tctb_datasource_u_uo |  | fuseorgid |
