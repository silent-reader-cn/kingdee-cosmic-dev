# 工单执行调度方案-mpdm_order_schedule

## 工单执行调度方案-主表 t_mpdm_orderschedule

- **表名称：** 工单执行调度方案-主表
- **表名：** t_mpdm_orderschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpomshutdowninqtytype | 入库数量合计 | varchar | 30 |  | √ | ' ' | 入库数量合计,枚举: A :合格品入库数量 B :不合格品入库数量 C :报废品入库数量 |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frepeat | 重复运算 | bpchar | 1 |  | √ | ' ' | 重复运算 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fisrelease | 已发布 | bpchar | 1 |  | √ | ' ' | 已发布 |
| 7 | fpredtime | 时间 | int4 | 32 |  | √ | 0 | 时间 |
| 8 | fpomshutdowncondition | 关闭条件 | bpchar | 1 |  | √ | ' ' | 关闭条件,枚举: A :入库数量达到工单数量 B :入库数量达到入库下限数量 C :入库数量达到入库上限数量 D :入库数量达到预计产出数量 |
| 9 | frunningtype | 运行时间类型 | varchar | 5 |  | √ | ' ' | 运行时间类型,枚举: 0 :立即运算 1 :预约时间运算 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanid | 调度方案ID | varchar | 50 |  | √ | ' ' | 调度方案ID |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fdaysofmon | 月 | varchar | 50 |  | √ | ' ' | 月 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdaysofweek | 周 | varchar | 50 |  | √ | ' ' | 周 |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fpomendworkcondition | 完工条件 | bpchar | 1 |  | √ | ' ' | 完工条件,枚举: A :入库数量达到工单数量 B :入库数量达到入库下限数量 C :入库数量达到入库上限数量 D :入库数量达到预计产出数量 |
| 20 | fjobid | 调度任务ID | varchar | 50 |  | √ | ' ' | 调度任务ID |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fpomendworkinqtytype | 入库数量合计 | varchar | 30 |  | √ | ' ' | 入库数量合计,枚举: A :合格品入库数量 B :不合格品入库数量 C :报废品入库数量 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | frepeattype | 时间重复类型 | varchar | 50 |  | √ | ' ' | 时间重复类型,枚举: 0 :周 1 :月 |
| 25 | frunstatus | 运行状态 | bpchar | 1 |  | √ | ' ' | 运行状态,枚举: A :未运行 B :运行中 C :异常终止 D :正常结束 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_orderschedule |  | fid |
| 2 | idx_mpdm_orderschedule |  | fnumber |

---

## 生产组织-多选基础资料表 t_mpdm_orderschedule_peo

- **表名称：** 生产组织-多选基础资料表
- **表名：** t_mpdm_orderschedule_peo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_orderschedule_peo |  | fpkid |

---

## 工单执行调度方案-多语言表 t_mpdm_orderschedule_l

- **表名称：** 工单执行调度方案-多语言表
- **表名：** t_mpdm_orderschedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_orderschedule_l |  | fid,flocaleid |
| 2 | pk_t_mpdm_orderschedule_l |  | fpkid |

---

## 生产组织-多选基础资料表 t_mpdm_orderschedule_pso

- **表名称：** 生产组织-多选基础资料表
- **表名：** t_mpdm_orderschedule_pso

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_orderschedule_pso |  | fpkid |
