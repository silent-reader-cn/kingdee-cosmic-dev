# 发货状态-ococic_deliverstatus

## 发货状态-主表 t_ocdbd_deliverstatus

- **表名称：** 发货状态-主表
- **表名：** t_ocdbd_deliverstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fisreturnreceipt | 退货允许入库 | bpchar | 1 |  | √ | '0' | 退货允许入库 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fisallowdeliver | 是否允许退货 | bpchar | 1 |  | √ | '1' | 是否允许退货 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fisallowrefund | 是否允许直接退款 | bpchar | 1 |  | √ | '1' | 是否允许直接退款 |
| 13 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 ocdbd_biztype |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_deliverstatus |  | fid |
| 2 | idx_ocdbd_deliverstatus_num |  | fnumber |

---

## 发货状态-多语言表 t_ocdbd_deliverstatus_l

- **表名称：** 发货状态-多语言表
- **表名：** t_ocdbd_deliverstatus_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 发货状态名称 | varchar | 80 |  | √ | ' ' | 发货状态名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_deliverstatesl_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_deliverstatus_l |  | fpkid |
