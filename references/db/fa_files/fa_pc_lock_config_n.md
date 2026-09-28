# 总分锁配置-fa_pc_lock_config_n

## 持锁父单据定义单据体-子表 t_fa_hold_pclock_bill_n

- **表名称：** 持锁父单据定义单据体-子表
- **表名：** t_fa_hold_pclock_bill_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparentbillentitycode | 单据编码 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpentrycode | 分录编码 | varchar | 50 |  | √ | ' ' | 分录编码 |
| 4 | fprelbasetype | 引用基础资料类型 | varchar | 50 |  | √ | ' ' | 引用基础资料类型,枚举: HEAD :单据头 ONEENTITY :一级分录 UNSUPPORTED :定义不支持（代码实现） |
| 5 | fpentrybasecode | 分录基础资料编码 | varchar | 50 |  | √ | ' ' | 分录基础资料编码 |
| 6 | fpheadbasecode | 单头基础资料编码 | varchar | 50 |  | √ | ' ' | 单头基础资料编码 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_hold_pclock_uniquen |  | fid,fparentbillentitycode |
| 2 | pk_fa_hold_pclock_billn |  | fentryid |

---

## 总分锁配置-主表 t_fa_pc_lock_config_n

- **表名称：** 总分锁配置-主表
- **表名：** t_fa_pc_lock_config_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fstatuscode | 业务状态字段编码 | varchar | 256 |  | √ | ' ' | 业务状态字段编码 |
| 7 | fstatuscoment | 状态说明 | varchar | 256 |  | √ | ' ' | 状态说明 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | flockedentitycode | 被锁基础资料 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbiznormalstatus | 业务正常状态值 | varchar | 50 |  | √ | ' ' | 业务正常状态值 |
| 12 | fbizfinalstatus | 业务终态值 | varchar | 50 |  | √ | ' ' | 业务终态值 |
| 13 | fusepurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: default :默认 unittest :单元测试 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_pc_lock_confign |  | fid |
| 2 | idx_fa_pc_lock_config_purposen |  | flockedentitycode,fusepurpose |

---

## 持锁子单据定义单据体-子表 t_fa_hold_cclock_bill_n

- **表名称：** 持锁子单据定义单据体-子表
- **表名：** t_fa_hold_cclock_bill_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheadbasecode | 单头基础资料编码 | varchar | 50 |  | √ | ' ' | 单头基础资料编码 |
| 3 | fcentrybasecode | 分录基础资料编码 | varchar | 50 |  | √ | ' ' | 分录基础资料编码 |
| 4 | fcentrycode | 分录编码 | varchar | 50 |  | √ | ' ' | 分录编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcrelbasetype | 引用基础资料类型 | varchar | 50 |  | √ | ' ' | 引用基础资料类型,枚举: HEAD :单据头 ONEENTITY :一级分录 UNSUPPORTED :定义不支持（代码实现） |
| 8 | fchildbillentitycode | 单据编码 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_hold_cclock_billn |  | fentryid |
| 2 | idx_fa_hold_cclock_uniquen |  | fid,fchildbillentitycode |

---

## 父单据状态定义单据体-子表 t_fa_base_status_ctr_n

- **表名称：** 父单据状态定义单据体-子表
- **表名：** t_fa_base_status_ctr_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftobizstatus | 操作后状态 | varchar | 50 |  | √ | ' ' | 操作后状态 |
| 2 | ffrombizstatus | 操作前状态值 | varchar | 50 |  | √ | ' ' | 操作前状态值 |
| 3 | fcomment | 说明 | varchar | 256 |  | √ | ' ' | 说明 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | foperations | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: save :保存 submit :提交 audit :审核 unaudit :反审核 delete :删除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_base_status_ctrn |  | fentryid |
| 2 | pk_t_fa_base_status_ctrn |  | fdetailid |
