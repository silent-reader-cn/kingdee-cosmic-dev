# 不良品处理方式-bd_badhandmode

## 不良品处理方式-多语言表 t_qcbd_badhandmode_l

- **表名称：** 不良品处理方式-多语言表
- **表名：** t_qcbd_badhandmode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_badhandmode_l |  | fpkid |

---

## 不良品处理方式-主表 t_qcbd_badhandmode

- **表名称：** 不良品处理方式-主表
- **表名：** t_qcbd_badhandmode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fispreset | 系统预设 | varchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fcheckstate | 检验状态标识 | bpchar | 1 |  | √ | '1' | 检验状态标识,枚举: 0 :合格 1 :不合格 2 :不合格可出/入库 |
| 14 | foldbaddealstyle | 不良处理方式历史携带值 | varchar | 5 |  | √ | ' ' | 不良处理方式历史携带值 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_badhandmode |  | fid |
| 2 | uidx_qcbd_badhandmode_billno |  | fnumber |
| 3 | idx_t_qcbd_badhandmode |  | fcreatetime |

---

## 单据体-子表 t_qcbd_badhandentry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_badhandentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillformid | 单据 | varchar | 255 |  | √ | '0' | 主实体对象 bos_entityobject |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodebilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 7 | fispresetentry | 是否预设 | varchar | 1 |  | √ | '0' | 是否预设 |
| 8 | fisshow | 是否显示 | varchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_badhandentry |  | fentryid |
