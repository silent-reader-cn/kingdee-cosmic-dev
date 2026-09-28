# 外购物料标准价目表(废弃)-cad_purprices

## 外购物料标准价目表(废弃)-多语言表 t_cad_purprices_l

- **表名称：** 外购物料标准价目表(废弃)-多语言表
- **表名：** t_cad_purprices_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_purprices_l_pkey |  | fpkid |
| 2 | index_cad_purprices_l_df |  | fid,flocaleid |

---

## 外购物料标准价目表(废弃)-主表 t_cad_purprices

- **表名称：** 外购物料标准价目表(废弃)-主表
- **表名：** t_cad_purprices

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | famount | 标准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 标准金额 |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fistoupdate | 是否待更新 | bpchar | 1 |  | √ | '0' | 是否待更新 |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 14 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 15 | fbomversionid | fbomversionid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdatasrc | 数据来源 | varchar | 30 |  | √ | 'manual' | 数据来源,枚举: manual :手工新增 contract :采购合同 order :采购订单 costupdate :成本更新 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fmatcostid | 物料成本信息ID | int8 | 64 |  | √ | 0 | 物料成本信息ID |
| 24 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 25 | fbusinessctrl | fbusinessctrl | varchar | 30 |  | √ | ' ' |  |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_purprices_df |  | fcosttypeid,fmaterialid,fauxptyid,fmatversionid |
| 2 | t_cad_purprices_pkey |  | fid |
| 3 | idx_cad_purprices_kc |  | fkeycol |

---

## 物料对应成本子要素信息-子表 t_cad_purpricesentry

- **表名称：** 物料对应成本子要素信息-子表
- **表名：** t_cad_purpricesentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 3 | frate | 比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 比率(%) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fprice | 标准单价 | numeric | 23 | 10 | √ | 0.0000000000 | 标准单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_purpricesentry |  | fid,felementid,fsubelementid |
| 2 | t_cad_purpricesentry_pkey |  | fentryid |
