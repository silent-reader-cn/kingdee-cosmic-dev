# 保证金批量预提处理-fbd_surety_preint_batch

## 结息记录-子表 t_fbd_intbill_batch_entry

- **表名称：** 结息记录-子表
- **表名：** t_fbd_intbill_batch_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintcomment | 结息摘要 | varchar | 255 |  | √ | ' ' | 结息摘要 |
| 3 | floanbillid | 保证金id | int8 | 64 |  | √ | 0 | 保证金id |
| 4 | floanbillno | 保证金单编号 | varchar | 50 |  | √ | ' ' | 保证金单编号 |
| 5 | fintdetail_tag | 利息明细_详情 | text | 0 |  |  | null | 利息明细_详情 |
| 6 | fintdetail | 利息明细 | varchar | 255 |  | √ | ' ' | 利息明细 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fintdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 9 | factualinstamt | 实际预提金额 | numeric | 23 | 10 | √ | 0 | 实际预提金额 |
| 10 | fintdetailnum | 预提记录编号 | varchar | 50 |  | √ | ' ' | 预提记录编号 |
| 11 | fenddate | 计息结束日期 | timestamp | 0 |  |  | null | 计息结束日期 |
| 12 | fstatus | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: success :成功 fail :失败 |
| 13 | frate | 计息利率 | numeric | 17 | 6 | √ | 0 | 计息利率 |
| 14 | fstartdate | 计息开始日期 | timestamp | 0 |  |  | null | 计息开始日期 |
| 15 | fintbillid | 结息记录id | int8 | 64 |  | √ | 0 | 结息记录id |
| 16 | finttype | 利息类别 | varchar | 50 |  | √ | ' ' | 利息类别,枚举: lsbq :利随本清 jx :结息 |
| 17 | fisreverse | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcurrencyid | 存款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | finterestamt | 预提金额 | numeric | 23 | 10 | √ | 0 | 预提金额 |
| 21 | fcompanyid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | ffinorginfoid | 存款金融机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_intbillbatch_entry |  | fid |
| 2 | pk_fbd_intbill_batch_entry |  | fentryid |

---

## 保证金批量预提处理-多语言表 t_fbd_intbill_batch_l

- **表名称：** 保证金批量预提处理-多语言表
- **表名：** t_fbd_intbill_batch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_intbill_batch_l |  | fpkid |
| 2 | idx_fbd_intbill_batch_l |  | fid |

---

## 保证金批量预提处理-主表 t_fbd_intbill_batch

- **表名称：** 保证金批量预提处理-主表
- **表名：** t_fbd_intbill_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frevenuetype | frevenuetype | varchar | 50 |  | √ | ' ' |  |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: preint :预提利息 loan :贷款利息 currentint :存款结息 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | foperatetype | 操作类别 | varchar | 50 |  | √ | ' ' | 操作类别,枚举: preint :预提利息 reverseint :冲销预提利息 |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_intbillbatch_bnd |  | fbillno |
| 2 | pk_fbd_intbill_batch |  | fid |
