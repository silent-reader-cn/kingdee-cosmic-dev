# 支付链路数据_归档-fcs_payaccess_record_h

## 支付链路数据_归档-主表 t_fcs_payaccess_record_h

- **表名称：** 支付链路数据_归档-主表
- **表名：** t_fcs_payaccess_record_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdestbillpkid | 目标单主键id | int8 | 64 |  | √ | 0 | 目标单主键id |
| 3 | fnewway | 新增方式 | varchar | 30 |  | √ | ' ' | 新增方式,枚举: botp :BOTP下推 code :代码下推 custom :自定义 |
| 4 | ffulllinkid | 全链路ID | varchar | 2000 |  | √ | ' ' | 全链路ID |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fsrcentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 7 | fdestentity | 目标单实体 | varchar | 50 |  | √ | ' ' | 目标单实体 |
| 8 | fsrcidprop | 源单id属性 | varchar | 30 |  | √ | ' ' | 源单id属性,枚举: entry :分录 head :单头 |
| 9 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fdestbillid | 目标单id | int8 | 64 |  | √ | 0 | 目标单id |
| 14 | ferrormessage | 错误信息提示 | varchar | 255 |  | √ | ' ' | 错误信息提示 |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsrcbillpkid | 源单主键id | int8 | 64 |  | √ | 0 | 源单主键id |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fisrepeatresult | 重推 | bpchar | 1 |  | √ | '0' | 重推 |
| 20 | fbatchno | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 21 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 24 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 25 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fdestidprop | 目标单id属性 | varchar | 30 |  | √ | ' ' | 目标单id属性,枚举: entry :分录 head :单头 |
| 27 | fsrcentryprop | 源单分录属性 | varchar | 50 |  | √ | ' ' | 源单分录属性 |
| 28 | fdestentryprop | 目标单分录属性 | varchar | 50 |  | √ | ' ' | 目标单分录属性 |
| 29 | fisexcessresult | 超额 | bpchar | 1 |  | √ | '0' | 超额 |
| 30 | fsuccess | 完成 | bpchar | 1 |  | √ | '0' | 完成 |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_record_h_destid |  | fisrepeatresult,fisexcessresult,fdestbillid |
| 2 | idx_record_h_destpkid |  | fdestbillpkid |
| 3 | pk_t_fcs_payaccess_record_h |  | fid |
| 4 | idx_record_h_srcpkid |  | fsrcbillpkid |

---

## 支付链路数据_归档-多语言表 t_fcs_payaccess_record_h_l

- **表名称：** 支付链路数据_归档-多语言表
- **表名：** t_fcs_payaccess_record_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_payaccess_record_h_l |  | fid,flocaleid |
| 2 | pk_t_fcs_payaccess_record_h_l |  | fpkid |
