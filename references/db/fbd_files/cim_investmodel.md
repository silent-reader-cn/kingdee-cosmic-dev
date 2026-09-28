# 投资模型-cim_investmodel

## 投资模型-多语言表 t_cim_investmodel_l

- **表名称：** 投资模型-多语言表
- **表名：** t_cim_investmodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cim_investmodel_l |  | fpkid |
| 2 | idx_cim_investmodel_l |  | fid,flocaleid |

---

## 指定币别-多选基础资料表 t_cim_investmodel_cur

- **表名称：** 指定币别-多选基础资料表
- **表名：** t_cim_investmodel_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cim_investmodel_cur |  | fid |
| 2 | pk_cim_investmodel_cur |  | fpkid |

---

## 投资模型-主表 t_cim_investmodel

- **表名称：** 投资模型-主表
- **表名：** t_cim_investmodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feffectrule | 收益生效规则 | varchar | 30 |  | √ | ' ' | 收益生效规则,枚举: valuedate :理财起始日 iousintdate :起息日 |
| 3 | frevenueadjustrule | 收益日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 收益日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fgraceadjustrule | 赎回节假日规则 | varchar | 30 |  | √ | ' ' | 赎回节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 6 | fintcalmethod | 利息计算方法 | varchar | 30 |  | √ | ' ' | 利息计算方法,枚举: totalcallint :积数计息法 onecallint :逐笔计息法（按日） periodcallint :逐笔计息法（按期） |
| 7 | fisquotalimit | 是否控制限额 | bpchar | 1 |  | √ | '0' | 是否控制限额 |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | finvestvarietiesid | 投资品种 | int8 | 64 |  | √ | 0 | 投资品种 cim_investvarieties |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fprofitway | 收益方式 | varchar | 30 |  | √ | ' ' | 收益方式,枚举: redeem :赎回/解活时获取收益 fixedfrequency :固定频率收益 |
| 15 | fcurrencyrule | 币别规则 | varchar | 30 |  | √ | ' ' | 币别规则,枚举: nocurrency :不分币别 foreigncurrency :按外币 basecurrency :按本币 assigncurrency :指定币别 |
| 16 | frateresetadjustrule | 利率重置日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 利率重置日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 17 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 19 | fintheadtailrule | 计息头尾规则 | varchar | 30 |  | √ | ' ' | 计息头尾规则,枚举: headnotail :算头不算尾 noheadtail :算尾不算头 headtail :算头又算尾 noheadnotail :头尾都不算 |
| 20 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fpartytype | 交易对手类型 | varchar | 30 |  | √ | ' ' | 交易对手类型,枚举: bank :银行 finorg :非银行金融机构 other :其他 |
| 23 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 24 | frateresetdays | 利率重置偏移（d） | varchar | 30 |  | √ | ' ' | 利率重置偏移（d） |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | ftermtype | 期限类型 | varchar | 30 |  | √ | ' ' | 期限类型,枚举: short :短期 long :长期 nolimit :不限 indefinite :无期限 |
| 27 | fredeemway | 赎回/解活方式 | varchar | 30 |  | √ | ' ' | 赎回/解活方式,枚举: manual :手动到期赎回/解活 custom :自定义赎回/解活 |
| 28 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Actual/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 30 | frateadjustmethod | 利率重置方式 | varchar | 30 |  | √ | ' ' | 利率重置方式,枚举: noadjust :不重置 deadline :即时重置 cycle :周期性重置 hand :手工重置 |
| 31 | fprofittype | 收益类型 | varchar | 30 |  | √ | ' ' | 收益类型,枚举: cash :现金收益 share :份额收益 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 33 | fratetype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 34 | fintroundrule | 计息舍入规则 | varchar | 30 |  | √ | ' ' | 计息舍入规则,枚举: rounded :四舍五入 carry :无条件进位 give :无条件舍去 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cim_investmodel |  | fnumber,fstatus |
| 2 | pk_cim_investmodel |  | fid |
