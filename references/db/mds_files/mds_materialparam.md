# 物料分类备货参数-mds_materialparam

## 物料分类备货参数-主表 t_mds_materialparam

- **表名称：** 物料分类备货参数-主表
- **表名：** t_mds_materialparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | favgdelivery | 平均交期 | int8 | 64 |  | √ | 0 | 平均交期 |
| 4 | fdeliveryfactorno | 交期系数（非保质期） | int8 | 64 |  | √ | 0 | 交期系数（非保质期） |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fservicefactor | 服务系数 | varchar | 2000 |  | √ | ' ' | 服务系数 |
| 7 | fdelstandadev | 交期标准偏差 | numeric | 23 | 10 | √ | 0 | 交期标准偏差 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | facstockfactor | 设备库存系数 | varchar | 2000 |  | √ | ' ' | 设备库存系数 |
| 12 | finventorylevellow | 预测未来用量<目标库存水平，计算库存水平=： | varchar | 5 |  | √ | ' ' | 预测未来用量<目标库存水平，计算库存水平=：,枚举: 1 :目标库存水平 2 :预测未来用量 3 :目标库存水平和预测未来用量的平均值 |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fquarterfactor | 季度系数 | varchar | 2000 |  | √ | ' ' | 季度系数 |
| 16 | flongcycle | 长周期 | int8 | 64 |  | √ | 0 | 长周期 |
| 17 | finventorylevelhigh | 预测未来用量≥目标库存水平，计算库存水平=： | varchar | 5 |  | √ | ' ' | 预测未来用量≥目标库存水平，计算库存水平=：,枚举: 1 :目标库存水平 2 :预测未来用量 3 :目标库存水平和预测未来用量的平均值 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fstockfactor | 库存系数 | varchar | 2000 |  | √ | ' ' | 库存系数 |
| 20 | fdeliverydate | 交期系数 | varchar | 5 |  | √ | ' ' | 交期系数,枚举: 1 :实际交期 2 :计划交期 |
| 21 | fdeliveryfactor | 交期系数（保质期） | int8 | 64 |  | √ | 0 | 交期系数（保质期） |
| 22 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | favgqty | 平均用量 | varchar | 5 |  | √ | ' ' | 平均用量,枚举: 1 :总用量/总架数*使用概率 2 :总用量/总架数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_materialparam |  | fid |
| 2 | idx_mds_materialparam_no |  | fnumber |

---

## 物料分类备货参数-多语言表 t_mds_materialparam_l

- **表名称：** 物料分类备货参数-多语言表
- **表名：** t_mds_materialparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_materialparam_l_id |  | fid,flocaleid |
| 2 | pk_mds_materialparam_l |  | fpkid |
