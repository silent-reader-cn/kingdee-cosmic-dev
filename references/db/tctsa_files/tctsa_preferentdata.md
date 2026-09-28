# 优惠取数配置-tctsa_preferentdata

## 单据体-子表 t_tctsa_predata_entry

- **表名称：** 单据体-子表
- **表名：** t_tctsa_predata_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatasourcetext | 数据源 | varchar | 2000 |  | √ | ' ' | 数据源 |
| 3 | fstatisticprotid | 优惠项目 | int8 | 64 |  | √ | 0 | [统计项目 tctsa_statistic_project](../tctsa_files/tctsa_statistic_project.md) |
| 4 | frecheck | 是否复合 | varchar | 50 |  | √ | ' ' | 是否复合,枚举: 0 :否 1 :是 |
| 5 | fdatasourcejson | 数据源 | varchar | 255 |  | √ | ' ' | 数据源 |
| 6 | fdatasourcejson_tag | 数据源_详情 | text | 0 |  |  | null | 数据源_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | faccessfield | 取数字段 | varchar | 50 |  | √ | ' ' | 取数字段,枚举: |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_predata_entry |  | fentryid |
| 2 | idx_tctsa_predata_entry_fk |  | fid |

---

## 优惠取数配置-主表 t_tctsa_preferentdata

- **表名称：** 优惠取数配置-主表
- **表名：** t_tctsa_preferentdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaxationsysid | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 dkdj :代扣代缴 kjqysds :扣缴企业所得税 szys_a :水资源税A szys_b :水资源税B zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsybnsr_yz_fzjg :一般企业汇总申报预征方式分支机构 |
| 13 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 14 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctsa_prefd_tax |  | ftaxationsysid,ftaxcategoryid |
| 2 | pk_tctsa_preferentdata |  | fid |

---

## 优惠取数配置-多语言表 t_tctsa_preferentdata_l

- **表名称：** 优惠取数配置-多语言表
- **表名：** t_tctsa_preferentdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_preferentdata_l |  | fpkid |
| 2 | idx_tctsa_preferentdata_l_0 |  | fid,flocaleid |
