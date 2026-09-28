# 智能填充设置-cas_interpayplan

## 智能填充设置-多语言表 t_cas_interpayplan_l

- **表名称：** 智能填充设置-多语言表
- **表名：** t_cas_interpayplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_interpayplan_l |  | fpkid |

---

## 智能填充设置-主表 t_cas_interpayplan

- **表名称：** 智能填充设置-主表
- **表名：** t_cas_interpayplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 4 | fsettletype | 默认结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpaymentchannel | 默认支付渠道 | varchar | 30 |  | √ | ' ' | 默认支付渠道,枚举: bei :银企互联 onlinebank :网上银行 counter :柜台 |
| 7 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fusage | 默认转账附言 | varchar | 200 |  | √ | ' ' | 默认转账附言 |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fpayeracctbank | 默认付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | ffiltercon_tag | 使用条件内容_详情 | text | 0 |  |  | null | 使用条件内容_详情 |
| 16 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 17 | ffiltercon | 使用条件内容 | text | 0 |  |  | null | 使用条件内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_interpayplan_pkey |  | fid |
