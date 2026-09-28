# 资金池流水类型-ocdbd_balflowtype

## 资金池流水类型-主表 t_ocdbd_balflowtype

- **表名称：** 资金池流水类型-主表
- **表名：** t_ocdbd_balflowtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbalobjid | 余额表 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fupdatetype | 更新方向 | bpchar | 1 |  | √ | '0' | 更新方向,枚举: 0 :增加 1 :减少 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frollbackflowtypeid | 回滚流水类型 | int8 | 64 |  | √ | 0 | [资金池流水类型 ocdbd_balflowtype](../occba_files/ocdbd_balflowtype.md) |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | frollbacktrans | 回滚对应更新事务 | bpchar | 1 |  | √ | 'A' | 回滚对应更新事务,枚举: A :结算支付 B :余额冻结 C :单据使用 D :余额调整 E :资金使用 F :订单变更 G :余额释放 H :单据释放 I :订单关闭 J :订单反关闭 K :金额冻结 L :金额解冻 R :余额回滚 O :预算下达 P :预算撤销 Q :余额调整 S :单据使用 T :单据释放 U :单据关闭 V :单据反关闭 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fupdatetrans | 对应更新事务 | bpchar | 1 |  | √ | 'A' | 对应更新事务,枚举: A :结算支付 B :余额冻结 C :单据使用 D :余额调整 E :资金使用 F :订单变更 G :余额释放 H :单据释放 I :订单关闭 J :订单反关闭 K :金额冻结 L :金额解冻 R :余额回滚 O :预算下达 P :预算撤销 Q :余额调整 S :单据使用 T :单据释放 U :单据关闭 V :单据反关闭 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_balflowtype |  | fid |
| 2 | idx_ocdbd_balflowtype |  | fnumber |

---

## 资金池流水类型-多语言表 t_ocdbd_balflowtype_l

- **表名称：** 资金池流水类型-多语言表
- **表名：** t_ocdbd_balflowtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_balflowtype_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_balflowtype_l |  | fpkid |
