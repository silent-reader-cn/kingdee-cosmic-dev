# 材料核销记录-im_mdc_omwrfrecord

## 材料核销记录-主表 t_im_mdc_ommatrlwrfrecord

- **表名称：** 材料核销记录-主表
- **表名：** t_im_mdc_ommatrlwrfrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销批号 | varchar | 50 |  | √ | ' ' | 核销批号 |
| 3 | fmaincurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 6 | forgid | 核销组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsupply | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fwriteoffrela | fwriteoffrela | varchar | 50 |  | √ | ' ' |  |
| 12 | fheadwfinfo | 核销详情 | varchar | 255 |  | √ | ' ' | 核销详情 |
| 13 | fwfnumber | 核销编码 | varchar | 50 |  | √ | ' ' | 核销编码 |
| 14 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fheadwfinfo_tag | 核销详情_详情 | text | 0 |  |  | null | 核销详情_详情 |
| 16 | fwriteofftype | fwriteofftype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_ommatrlwrfrecord |  | fid |
| 2 | idx_t_im_mdc_ommatrl_fwnum |  | fwfnumber |

---

## 单据体-子表 t_im_mdc_ommatrlwrfentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_ommatrlwrfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 3 | fasstunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | finvscheme | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 5 | fasstsrcbillentryseq | 单据分录序号 | int8 | 64 |  | √ | 0 | 单据分录序号 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmaterielfield | 物料(隐藏) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 9 | fseq | 分录行号 | numeric | 10 |  | √ | 0 | 分录行号 |
| 10 | fverifybaseqty | 本次核销基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次核销基本数量 |
| 11 | funitfield | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 13 | fdatefield | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 14 | fsrcentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 15 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 16 | fasstmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 17 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 18 | fwfinfo | 核销详情 | varchar | 255 |  | √ | ' ' | 核销详情 |
| 19 | fwfinfo_tag | 核销详情_详情 | text | 0 |  |  | null | 核销详情_详情 |
| 20 | fasstbasewritqty | 本次核销数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次核销数量 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_matrlentry_fid |  | fid |
| 2 | pk_im_mdc_ommatrlwrfentry |  | fentryid |
