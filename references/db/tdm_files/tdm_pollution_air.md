# 大气污染信息-tdm_pollution_air

## 大气污染信息-多语言表 t_tdm_pollution_air_l

- **表名称：** 大气污染信息-多语言表
- **表名：** t_tdm_pollution_air_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 排放口名称 | varchar | 50 |  | √ | ' ' | 排放口名称 |
| 3 | fpollutionname | 污染物名称 | varchar | 50 |  | √ | ' ' | 污染物名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_pollution_air_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_pollution_air_l |  | fpkid |

---

## 大气污染信息-主表 t_tdm_pollution_air

- **表名称：** 大气污染信息-主表
- **表名：** t_tdm_pollution_air

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 5 | ffqpfl | 废气排放量 | numeric | 23 | 10 | √ | 0.0000000000 | 废气排放量 |
| 6 | fwrwpfl | 污染物排放量 | numeric | 23 | 10 | √ | 0.0000000000 | 污染物排放量 |
| 7 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fjsjs | 计算基数 | numeric | 23 | 10 | √ | 0.0000000000 | 计算基数 |
| 13 | fmonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fcwxs | 产污系数 | numeric | 23 | 10 | √ | 0.0000000000 | 产污系数 |
| 16 | fwrwdw | 污染物单位 | varchar | 30 |  | √ | ' ' | 污染物单位,枚举: ton :吨 kg :千克 g :克 mg :毫克 |
| 17 | fpwxs | 排污系数 | numeric | 23 | 10 | √ | 0.0000000000 | 排污系数 |
| 18 | fnumber | 税源编号 | varchar | 30 |  | √ | ' ' | 税源编号 |
| 19 | fcountmethod | 污染物排放量计算方法 | varchar | 30 |  | √ | ' ' | 污染物排放量计算方法,枚举: zdjc :自动监测 jcjgjc :监测机构监测 pwxs :排污系数 wlhs :物料衡算 |
| 20 | fscndz | 实测浓度值 | numeric | 23 | 10 | √ | 0.0000000000 | 实测浓度值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_pollution_air |  | fid |
| 2 | idx_tdm_pollution_air |  | forg |
