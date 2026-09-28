# 费用执行记录-ocmem_marketcostexecute

## 费用执行记录-多语言表 t_ocmem_mcostexecute_l

- **表名称：** 费用执行记录-多语言表
- **表名：** t_ocmem_mcostexecute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 执行名称 | varchar | 100 |  | √ | ' ' | 执行名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcostexecute_l |  | fpkid |
| 2 | idx_ocmem_mcel_fidflid |  | fid,flocaleid |

---

## 费用执行记录-主表 t_ocmem_mcostexecute

- **表名称：** 费用执行记录-主表
- **表名：** t_ocmem_mcostexecute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecommendation | 改进建议 | varchar | 510 |  | √ | ' ' | 改进建议 |
| 3 | fexecaddress | 执行地点 | varchar | 500 |  | √ | ' ' | 执行地点 |
| 4 | forgid | 所属部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbuyuserqty | 购买人数 | numeric | 23 | 10 | √ | 0 | 购买人数 |
| 6 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fbuyamount | 购买金额 | numeric | 23 | 10 | √ | 0 | 购买金额 |
| 12 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fsignuserqty | 签到人数 | numeric | 23 | 10 | √ | 0 | 签到人数 |
| 14 | fname | 执行名称 | varchar | 100 |  | √ | ' ' | 执行名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fexecuteeffect | 执行效果 | bpchar | 1 |  | √ | ' ' | 执行效果,枚举: A :非常好 B :较好 C :一般 D :不好 |
| 17 | fpicture3 | 图片3 | varchar | 255 |  | √ | ' ' | 图片3 |
| 18 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 19 | fpicture2 | 图片2 | varchar | 255 |  | √ | ' ' | 图片2 |
| 20 | fpicture1 | 图片1 | varchar | 255 |  | √ | ' ' | 图片1 |
| 21 | fdescription | 执行说明 | varchar | 500 |  | √ | ' ' | 执行说明 |
| 22 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fexecdevice | 执行设备ID | varchar | 500 |  | √ | ' ' | 执行设备ID |
| 25 | fnumber | 执行编码 | varchar | 80 |  | √ | ' ' | 执行编码 |
| 26 | fcostapplyentryid | 费用申请单分录 | int8 | 64 |  | √ | 0 | 市场费用申请单分录 ocmem_mcostapply_entry |
| 27 | fexecutetype | 执行类型 | bpchar | 1 |  | √ | ' ' | 执行类型,枚举: A :活动执行 B :费用执行 |
| 28 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fmarketcostbillid | 费用申请单编码 | int8 | 64 |  | √ | 0 | 市场费用申请单基础资料 ocmem_marketcost_applybd |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_mce_fceid |  | fcostapplyentryid |
| 2 | pk_ocmem_mcostexecute |  | fid |
| 3 | idx_ocmem_mce_fno |  | fnumber |

---

## 单据体-子表 t_ocmem_mcostexecutee

- **表名称：** 单据体-子表
- **表名：** t_ocmem_mcostexecutee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fthumbnailurlurl | 缩略图路径 | varchar | 255 |  | √ | ' ' | 缩略图路径 |
| 4 | fpicurl | 图片路径 | varchar | 200 |  | √ | ' ' | 图片路径 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_mcostexecutee |  | fentryid |
| 2 | idx_ocmem_mcee_fid |  | fid |
