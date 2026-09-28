# 用量概率分析结果-mds_probabilityresult

## 章节号-多选基础资料表 t_mds_probability_ata

- **表名称：** 章节号-多选基础资料表
- **表名：** t_mds_probability_ata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | ATA章节号 mpdm_atachapterno |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probability_ata |  | fpkid |
| 2 | idx_mds_probabi_ata_id |  | fid |

---

## 用量概率分析结果-主表 t_mds_probabilityresult

- **表名称：** 用量概率分析结果-主表
- **表名：** t_mds_probabilityresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplytype | 供应方式 | varchar | 50 |  | √ | ' ' | 供应方式,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | favgdelivery | 三年平均交期 | numeric | 23 | 10 | √ | 0 | 三年平均交期 |
| 5 | faccount | 总架数 | numeric | 23 | 10 | √ | 0 | 总架数 |
| 6 | flogid | 计算日志 | int8 | 64 |  | √ | 0 | 用量概率计算日志 mds_probabilitylog |
| 7 | flifecontrol | 是否保质期 | bpchar | 1 |  | √ | '0' | 是否保质期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 10 | fsupplier | 供应方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | flastdelivery | 最近一次交期 | numeric | 23 | 10 | √ | 0 | 最近一次交期 |
| 13 | fconmtypenumber | 合同类型编码 | varchar | 2000 |  | √ | ' ' | 合同类型编码 |
| 14 | fsuggestamount | 建议采购金额 | numeric | 23 | 10 | √ | 0 | 建议采购金额 |
| 15 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fsuggestqty | 建议数量 | numeric | 23 | 10 | √ | 0 | 建议数量 |
| 17 | fusemonthcount | 使用月数 | numeric | 23 | 10 | √ | 0 | 使用月数 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fcontracttype | 合同类型（旧版） | varchar | 50 |  | √ | ' ' | 合同类型（旧版）,枚举: VMI CONSIGNMENT :VMI CONSIGNMENT NON-VMI CONSIGNMENT :NON-VMI CONSIGNMENT TERMS CONTRACT :TERMS CONTRACT |
| 20 | fqty | 总数量 | numeric | 23 | 10 | √ | 0 | 总数量 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fbackupproject | 备货项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 26 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fcountdim | 统计维度 | varchar | 5 |  | √ | ' ' | 统计维度,枚举: 1 :项目 2 :工卡 |
| 28 | fconmtypename | 合同类型名称 | varchar | 2000 |  | √ | ' ' | 合同类型名称 |
| 29 | factype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 30 | flastamount | 最新采购单价（RMB） | numeric | 23 | 10 | √ | 0 | 最新采购单价（RMB） |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fconmtypeid | 合同类型ID | varchar | 2000 |  | √ | ' ' | 合同类型ID |
| 33 | fmaterialtype | 物料类型 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 34 | fsupplyresp | 供货责任 | varchar | 50 |  | √ | ' ' | 供货责任,枚举: 0 :库存组织 1 :客户 2 :VMI供应商 3 :非VMI供应商 |
| 35 | flevel | 频率等级 | varchar | 50 |  | √ | ' ' | 频率等级 |
| 36 | fanalysisdim | 分析维度 | varchar | 5 |  | √ | ' ' | 分析维度,枚举: A :客户+检修设备类型+检修级别 B :客户+检修设备类型 C :检修设备类型 |
| 37 | fmaxqty | 最大用量 | numeric | 23 | 10 | √ | 0 | 最大用量 |
| 38 | fuseaccount | 使用该件号的架数 | numeric | 23 | 10 | √ | 0 | 使用该件号的架数 |
| 39 | favgqty | 平均用量 | numeric | 23 | 10 | √ | 0 | 平均用量 |
| 40 | fuseprobability | 概率 | numeric | 23 | 10 | √ | 0 | 概率 |
| 41 | fminqty | 最小用量 | numeric | 23 | 10 | √ | 0 | 最小用量 |
| 42 | fcard | 工卡 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fmaterialname | fmaterialname | varchar | 200 |  | √ | ' ' |  |
| 45 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 46 | fatanumber | 章节号(废弃) | varchar | 255 |  | √ | ' ' | 章节号(废弃) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probabilityresult |  | fid |
| 2 | idx_mds_probabilityresult |  | flogid |
