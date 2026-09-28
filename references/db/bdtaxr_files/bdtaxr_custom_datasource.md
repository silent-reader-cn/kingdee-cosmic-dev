# 数据源配置-bdtaxr_custom_datasource

## 数据源配置-主表 t_bdtaxr_datasource_conf

- **表名称：** 数据源配置-主表
- **表名：** t_bdtaxr_datasource_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 自定义数据源分组 | int8 | 64 |  | √ | 0 | [自定义数据源分组 tctb_datasource_group](../tctb_files/tctb_datasource_group.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbizname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 5 | fischild | 是否主子关系 | bpchar | 1 |  | √ | ' ' | 是否主子关系 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fentityname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsubentityname | 子实体名称 | varchar | 50 |  | √ | ' ' | 子实体名称 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fcondition | 关联条件 | varchar | 50 |  | √ | ' ' | 关联条件 |
| 17 | ftaxtype | 适用税种类型 | varchar | 50 |  | √ | ' ' | 适用税种类型,枚举: VAT_INCOME :增值税-收入取数规则 VAT_ROLLOUT :增值税-进项税额转出取数规则 VAT_DIFF :增值税-差额扣除取数规则 CSD_AQHZ :印花税-按期汇总 CSD_HDZS :印花税-核定征收 VAT_DEDUCTION :增值税-减税项目取数规则 CIT_YJ :企业所得税-预缴取数 VAT-PREPAY :增值税-预缴项目规则 CIT-ZCZJ :企业所得税-资产折旧摊销规则 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fuserorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | ftype | 表类型 | varchar | 50 |  | √ | ' ' | 表类型,枚举: 0 :自定义 1 :发票数据 2 :财务数据 3 :增值税台账 4 :增值税申报表 5 :所得税底稿 6 :所得税申报表季报 7 :所得税申报表年报 8 :所得税季报台账 9 :印花税 10 :房产税城镇土地使用税 11 :小规模申报表 12 :所得税申报表月报 13 :分支机构所得税申报表年报 14 :所得税核定征收月报 15 :所得税核定征收季报 16 :所得税核定征收年报 17 :小规模台账 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_datasource_conf |  | fid |
| 2 | idx_t_bdtaxr_datasource_conf_createorg |  | fcreateorgid |
| 3 | idx_bdtaxr_datasource_conf |  | fnumber |
| 4 | idx_t_bdtaxr_datasource_conf_master |  | fmasterid |

---

## 字段配置-子表 t_bdtaxr_datasource_entry

- **表名称：** 字段配置-子表
- **表名：** t_bdtaxr_datasource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwherestate | 过滤字段 | bpchar | 1 |  | √ | ' ' | 过滤字段 |
| 3 | finspectionshowfield | 抽检展示字段 | bpchar | 1 |  | √ | ' ' | 抽检展示字段 |
| 4 | fdescrice | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 5 | fsubname | 实体名称 | varchar | 50 |  | √ | ' ' | 实体名称 |
| 6 | felementwhere | 抽检条件字段 | bpchar | 1 |  | √ | ' ' | 抽检条件字段 |
| 7 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 8 | forgstate | 组织字段 | bpchar | 1 |  | √ | ' ' | 组织字段 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fisamount | 金额字段 | bpchar | 1 |  | √ | ' ' | 金额字段 |
| 11 | fyearstate | 年份字段 | bpchar | 1 |  | √ | ' ' | 年份字段 |
| 12 | fmonthstate | 月份字段 | bpchar | 1 |  | √ | ' ' | 月份字段 |
| 13 | fstate | 查询状态 | bpchar | 1 |  | √ | ' ' | 查询状态 |
| 14 | fdatastate | 时间字段 | bpchar | 1 |  | √ | ' ' | 时间字段 |
| 15 | fbizsubname | 业务名称 | varchar | 127 |  | √ | ' ' | 业务名称 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_datasource_entry |  | fentryid |
| 2 | idx_bdtaxr_datasource_entry |  | fid |

---

## 数据源配置-使用范围表 t_bdtaxr_datasource_conf_u

- **表名称：** 数据源配置-使用范围表
- **表名：** t_bdtaxr_datasource_conf_u

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
| 1 | idx_t_bdtaxr_datasource_conf_u_uo |  | fuseorgid |
| 2 | pk_t_bdtaxr_datasource_conf_u |  | fdataid,fuseorgid |

---

## 数据源配置-多语言表 t_bdtaxr_datasource_conf_l

- **表名称：** 数据源配置-多语言表
- **表名：** t_bdtaxr_datasource_conf_l

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
| 1 | pk_bdtaxr_datasource_conf_l |  | fpkid |
| 2 | idx_bdtaxr_datasource_conf_l_0 |  | fid,flocaleid |

---

## 数据源配置-使用范围位图表 t_bdtaxr_datasource_conf_m

- **表名称：** 数据源配置-使用范围位图表
- **表名：** t_bdtaxr_datasource_conf_m

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
| 1 | pk_t_bdtaxr_datasource_conf_m |  | forgid |
