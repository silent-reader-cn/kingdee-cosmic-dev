# 资产税务卡片-tdm_asset_taxc_card

## 资产税务卡片-主表 t_tdm_asset_taxc_card

- **表名称：** 资产税务卡片-主表
- **表名：** t_tdm_asset_taxc_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftaxdepreciation | 税务折旧方法 | int8 | 64 |  | √ | 0 | 税务折旧方法 tpo_tax_depreciation |
| 4 | fnetamount | 净额 | numeric | 23 | 10 | √ | 0 | 净额 |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdcleaningdate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 7 | ftaxaccountingbook | 税务账簿 | varchar | 50 |  | √ | ' ' | 税务账簿,枚举: ybzj :一般折旧 jszj :加速折旧 |
| 8 | ftaxsurplusdepperiods | 税务剩余折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务剩余折旧摊销期数 |
| 9 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 10 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 11 | fpolicyconfirmationstatus | 政策确认状态 | varchar | 50 |  | √ | ' ' | 政策确认状态,枚举: 0 :未确认 1 :已确认 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 14 | ftaxbase | 计税基础 | numeric | 23 | 10 | √ | 0 | 计税基础 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | faccdepreciationmethod | 会计折旧方法 | varchar | 200 |  | √ | ' ' | 会计折旧方法 |
| 19 | fassetsvalue | 会计资产原值 | numeric | 23 | 10 | √ | 0 | 会计资产原值 |
| 20 | fquicktaxassetclass | 税务加速折旧类别 | int8 | 64 |  | √ | 0 | 折旧政策分录 tpo_depreciation_detail |
| 21 | ftaxdepreciatedperiods | 税务已折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务已折旧摊销期数 |
| 22 | fassetdata | 资产编码 | int8 | 64 |  | √ | 0 | 资产清单 tdm_asset_data |
| 23 | ftaxamortizationperiods | 税务预计折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务预计折旧摊销期数 |
| 24 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 25 | ftaxcurrentdepamount | 税务当期折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务当期折旧摊销额 |
| 26 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | ftaxresidualvalue | 税务预计净残值 | numeric | 23 | 10 | √ | 0 | 税务预计净残值 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | frdaddition | 是否研发形成 | varchar | 50 |  | √ | ' ' | 是否研发形成,枚举: 1 :是 0 :否 |
| 31 | fbooktaxdifferenttype | 税会差异类型 | varchar | 50 |  | √ | ' ' | 税会差异类型,枚举: 0 :计税基础 1 :预计折旧摊销期数 2 :折旧方法 |
| 32 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | faccresidualvalue | 会计预计净残值 | numeric | 23 | 10 | √ | 0 | 会计预计净残值 |
| 34 | fnodepreciation | 不允许列支折旧 | varchar | 50 |  | √ | ' ' | 不允许列支折旧,枚举: assetsUseRight :使用权资产 noTaxIncomeAssets :不征税收入形成资产 notApplicable :不适用 |
| 35 | faccamortizationperiods | 会计预计折旧摊销期数 | int8 | 64 |  | √ | 0 | 会计预计折旧摊销期数 |
| 36 | ftaxaccumulateddepamount | 税务累计折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务累计折旧摊销额 |
| 37 | fassetclass | 会计资产类别 | varchar | 300 |  | √ | ' ' | 会计资产类别 |
| 38 | ftaxassetclass | 税务资产类别 | int8 | 64 |  | √ | 0 | 折旧政策分录 tpo_depreciation_detail |
| 39 | fbooktaxdifferent | 税会差异 | varchar | 50 |  | √ | ' ' | 税会差异,枚举: 1 :是 0 :否 |
| 40 | fdepreciationstatus | 折旧状态 | varchar | 50 |  | √ | ' ' | 折旧状态,枚举: 0 :未计算 1 :已计算 2 :已确认 3 :计算中 |
| 41 | fstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 42 | fassetuse | 资产用途 | varchar | 50 |  | √ | ' ' | 资产用途,枚举: au_0 :用于研发投入 au_1 :用于高新投入 |
| 43 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :系统同步 import :模板引入 manual :手工新增 |
| 45 | fnumber | 编码 | varchar | 250 |  | √ | ' ' | 编码 |
| 46 | fdepreciationadjustmethod | 折旧调整方式 | varchar | 50 |  | √ | ' ' | 折旧调整方式,枚举: wlsy :未来适用 zstz :追溯调整 |
| 47 | ftaxthisyeardepamount | 税务本年折旧摊销额 | numeric | 23 | 10 | √ | 0 | 税务本年折旧摊销额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_assettaxccard_assetdata |  | fassetdata,faccountingperiod,ftaxaccountingbook |
| 2 | pk_tdm_asset_taxc_card |  | fid |

---

## 资产税务卡片-多语言表 t_tdm_asset_taxc_card_l

- **表名称：** 资产税务卡片-多语言表
- **表名：** t_tdm_asset_taxc_card_l

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
| 1 | idx_tdm_asset_taxc_card_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_asset_taxc_card_l |  | fpkid |
