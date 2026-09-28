# 控制单据注册-xkbm_registerentity

## 控制单据注册-多语言表 t_xkbm_registerentity_l

- **表名称：** 控制单据注册-多语言表
- **表名：** t_xkbm_registerentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fappname | 所属应用 | varchar | 255 |  | √ | ' ' | 所属应用 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_registerentity_l |  | fid,flocaleid |
| 2 | pk_xkbm_registerentity_l |  | fpkid |

---

## 状态映射单据体-子表 t_xkbm_regentitystatus

- **表名称：** 状态映射单据体-子表
- **表名：** t_xkbm_regentitystatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatusfield | 对应状态字段 | varchar | 50 |  | √ | ' ' | 对应状态字段,枚举: billstatus :单据状态 |
| 3 | fstandardstatus | 纳入统计的受控状态 | varchar | 50 |  | √ | ' ' | 纳入统计的受控状态,枚举: save :暂存 submit :已提交 audit :已审核 close :已关闭 |
| 4 | fstatuseffecttypes | 适用预算影响类型范围 | varchar | 50 |  | √ | ' ' | 适用预算影响类型范围,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fstatusrange | 对应单据状态范围 | varchar | 1000 |  | √ | ' ' | 对应单据状态范围,枚举: billstatus-A :暂存 billstatus-B :已提交 billstatus-C :已审核 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fstatuskeys | 单据状态标识 | varchar | 1000 |  | √ | ' ' | 单据状态标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_regentitystatus_fid |  | fid |
| 2 | pk_xkbm_regentitystatus |  | fentryid |

---

## 控制单据注册-主表 t_xkbm_registerentity

- **表名称：** 控制单据注册-主表
- **表名：** t_xkbm_registerentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 所属应用 | int8 | 64 |  | √ | 0 | 控制单据注册分组 xkbm_regentitygroup |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fappid | 业务应用实体 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | feffecttypes | 预算影响类型 | varchar | 50 |  | √ | ' ' | 预算影响类型,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 13 | fappname | 所属应用 | varchar | 255 |  | √ | ' ' | 所属应用 |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fcommonplan | 公用 | bpchar | 1 |  | √ | '0' | 公用 |
| 19 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fenablecontrolop | 自定义受控操作 | bpchar | 1 |  | √ | '0' | 自定义受控操作 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbaseentity | 单据对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_registerentity |  | fnumber |
| 2 | pk_xkbm_registerentity |  | fid |

---

## 操作映射单据体-子表 t_xkbm_cusopentry

- **表名称：** 操作映射单据体-子表
- **表名：** t_xkbm_cusopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolopkey | 自定义操作标识 | varchar | 50 |  | √ | ' ' | 自定义操作标识 |
| 3 | fequalop | 等同于标准受控操作 | varchar | 50 |  | √ | ' ' | 等同于标准受控操作,枚举: submit :提交 audit :审核 unsubmit :撤销提交 unaudit :反审核 |
| 4 | fopeffecttypes | 适用预算影响类型范围 | varchar | 50 |  | √ | ' ' | 适用预算影响类型范围,枚举: 1 :申请占用 2 :预算执行 3 :预算冲回 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcontrolop | 自定义受控操作 | varchar | 50 |  | √ | ' ' | 自定义受控操作,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_cusopentry |  | fentryid |
| 2 | idx_xkbm_cusopentry_fid |  | fid |
