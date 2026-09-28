# 电票直连设置-bei_electicdirconset

## 电票直连设置-主表 t_bei_electicdirconset

- **表名称：** 电票直连设置-主表
- **表名：** t_bei_electicdirconset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdefaultaccount | 默认票据账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbankname | 开户行行号 | varchar | 50 |  | √ | ' ' | 开户行行号 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdirectconnchannelid | 直连渠道 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 17 | fbankinterface | 银企接口 | varchar | 50 |  | √ | ' ' | 银企接口,枚举: |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_electicdirconset |  | fid |
| 2 | idx_bei_electicdirconset |  | fnumber |

---

## 电票直连设置-多语言表 t_bei_electicdirconset_l

- **表名称：** 电票直连设置-多语言表
- **表名：** t_bei_electicdirconset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_electicdirconset_l |  | fid |
| 2 | pk_t_bei_electicdirconset_l |  | fpkid |
