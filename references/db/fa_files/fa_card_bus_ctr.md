# 实物卡片业务控制-fa_card_bus_ctr

## 实物卡片业务控制-主表 t_fa_card_bus_ctr

- **表名称：** 实物卡片业务控制-主表
- **表名：** t_fa_card_bus_ctr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 3 | fsrcbillentityname | 源单据标识 | varchar | 30 |  | √ | ' ' | 源单据标识 |
| 4 | fsublocknum | 子锁次数 | int8 | 64 |  | √ | 0 | 子锁次数 |
| 5 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: ADD :新增 READY :就绪 CHG :变更 DEPRE :折旧 CLEAR_ALL :完全清理 CLEAR_PART :部分清理 DISPATCH :调拨 SPLIT :拆分 COMBIN :组合 DELETE :作废 TRANSFERING :移交中 DRAWBACKING :退库中 SIGNED :已签收 DEVALUE :减值 DEPREADJUST :折旧调整 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_bus_ctr |  | fsrcbillid |
| 2 | pk_fa_card_bus_ctr |  | fid |

---

## 单据体-子表 t_fa_card_bus_ctr_detail

- **表名称：** 单据体-子表
- **表名：** t_fa_card_bus_ctr_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdtmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fdtholdlockentityname | 持锁单据标识 | varchar | 36 |  | √ | ' ' | 持锁单据标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdtholdlockdataid | 持锁数据ID | int8 | 64 |  | √ | 0 | 持锁数据ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_card_bus_ctr_detail |  | fentryid |
| 2 | idx_fa_card_bus_ctr_detail |  | fid,fdtholdlockdataid,fdtholdlockentityname |
