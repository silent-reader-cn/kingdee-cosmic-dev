# 减免性质代码申报映射-tsate_jmxzdm_mapping

## 减免性质代码申报映射-多语言表 t_tsate_jmxzdm_mapping_l

- **表名称：** 减免性质代码申报映射-多语言表
- **表名：** t_tsate_jmxzdm_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 减免项目名称 | varchar | 200 |  | √ | ' ' | 减免项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_jmxzdm_mapping_l |  | fpkid |
| 2 | idx_tsate_jmxzdm_mapping_l_0 |  | fid,flocaleid |

---

## 减免性质代码申报映射-主表 t_tsate_jmxzdm_mapping

- **表名称：** 减免性质代码申报映射-主表
- **表名：** t_tsate_jmxzdm_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 减免项目名称 | varchar | 200 |  | √ | ' ' | 减免项目名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fjmxzdm | 减免性质代码 | varchar | 50 |  | √ | ' ' | 减免性质代码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdiscount | 优惠项目 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftype | 申报税种 | varchar | 50 |  | √ | ' ' | 申报税种,枚举: qysdsjb :预缴申报 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码(对应减免事项代码) | varchar | 30 |  | √ | ' ' | 编码(对应减免事项代码) |
| 14 | fdiscountfb | 项目取数 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 15 | fchannel | 申报通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_jmxzdm_chan |  | fchannel,ftype |
| 2 | pk_tsate_jmxzdm_mapping |  | fid |
