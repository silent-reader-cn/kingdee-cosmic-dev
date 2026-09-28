# 预收款控制规则-occba_moneyusesetting

## 预收款控制规则-多语言表 t_occba_moneyuseset_l

- **表名称：** 预收款控制规则-多语言表
- **表名：** t_occba_moneyuseset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_moneyuseset_l |  | fpkid |
| 2 | idx_occba_moneytypesetl_flid |  | fid,flocaleid |

---

## 渠道范围单据体-子表 t_occba_controlarea

- **表名称：** 渠道范围单据体-子表
- **表名：** t_occba_controlarea

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyrelationid | 供货关系Id | int8 | 64 |  | √ | 0 | 供货关系Id |
| 3 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | flogicalrealtion | 逻辑关系 | bpchar | 1 |  | √ | '0' | 逻辑关系,枚举: 0 :包含关系 1 :例外排除 |
| 9 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_controlarea_fid |  | fid |
| 2 | pk_occba_controlarea |  | fentryid |

---

## 预收款控制规则-主表 t_occba_moneyuseset

- **表名称：** 预收款控制规则-主表
- **表名：** t_occba_moneyuseset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmoneyaccountid | 资金池账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcontroltype | 控制强度 | bpchar | 1 |  | √ | '0' | 控制强度,枚举: 0 :控制 1 :预警提示 2 :不控制 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fpaytype | 付款方式 | varchar | 20 |  | √ | ' ' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 10 | fupdatemoneytime | 扣除余额时点 | bpchar | 1 |  | √ | '0' | 扣除余额时点,枚举: 0 :提交 1 :审核 2 :无 |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbillentityid | 业务单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fcontroltime | 控制时点 | bpchar | 1 |  | √ | '0' | 控制时点,枚举: 0 :提交 1 :审核 2 :无 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_moneyuseset |  | fid |
| 2 | idx_occba_moneyuseset_num |  | fnumber |

---

## 单据类型-多选基础资料表 t_occba_usesetbilltype

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_occba_usesetbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_usesetbilltype_fbid |  | fid,fbasedataid |
| 2 | pk_occba_usesetbilltype |  | fpkid |
