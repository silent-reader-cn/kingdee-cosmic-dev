# 渠道目标-occbo_channelgoals

## 渠道目标-主表 t_occbo_channelgoals

- **表名称：** 渠道目标-主表
- **表名：** t_occbo_channelgoals

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 目标说明 | varchar | 255 |  | √ | ' ' | 目标说明 |
| 3 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fgoalsyearid | 目标年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 9 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fisautocalculate | 自动统计目标值 | bpchar | 1 |  | √ | '1' | 自动统计目标值 |
| 12 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fgoalstype | 目标类型 | bpchar | 1 |  | √ | ' ' | 目标类型,枚举: A :年度目标 B :月度目标 |
| 17 | fgoalsmap | 年月对应分录关系 | varchar | 2000 |  | √ | ' ' | 年月对应分录关系 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 目标编码 | varchar | 80 |  | √ | ' ' | 目标编码 |
| 20 | fdimension | KPI维度 | bpchar | 1 |  | √ | '1' | KPI维度,枚举: 0 :金额 1 :数量 |
| 21 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 22 | fkpiid | KPI | int8 | 64 |  | √ | 0 | KPI occbo_kpi_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals |  | fbillno |
| 2 | pk_occbo_channelgoals |  | fid |

---

## 渠道目标-多语言表 t_occbo_channelgoals_l

- **表名称：** 渠道目标-多语言表
- **表名：** t_occbo_channelgoals_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_chlgoals_l |  | fid,flocaleid |
| 2 | pk_occbo_channelgoals_l |  | fpkid |

---

## 目标月度-多选基础资料表 t_occbo_chlgoals_rp

- **表名称：** 目标月度-多选基础资料表
- **表名：** t_occbo_chlgoals_rp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_chlgoals_rp |  | fpkid |
| 2 | idx_occbo_chlgoals_rp |  | fid,fbasedataid |
