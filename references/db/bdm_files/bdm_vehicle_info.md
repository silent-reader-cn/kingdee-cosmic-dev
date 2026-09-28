# 车辆信息管理-bdm_vehicle_info

## 车辆信息管理-主表 t_bdm_vehicle_info

- **表名称：** 车辆信息管理-主表
- **表名：** t_bdm_vehicle_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproducingname | 生产企业名称 | varchar | 128 |  | √ | ' ' | 生产企业名称 |
| 3 | ftaxrate | 税率 | varchar | 10 |  | √ | ' ' | 税率,枚举: 0 :0% 0.015 :1.5% 0.01 :1% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 4 | fbrandmodel | 厂牌型号 | varchar | 80 |  | √ | ' ' | 厂牌型号 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fzerotaxmark | 零税率标识 | varchar | 10 |  | √ | ' ' | 零税率标识,枚举: 1 :免税 2 :不征税 3 :普通零税率 |
| 7 | ftaxpremark | 是否享受优惠政策 | varchar | 10 |  | √ | ' ' | 是否享受优惠政策,枚举: 0 :不享受 1 :享受 |
| 8 | fvehicletype | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型,枚举: 载货汽车 :载货汽车 越野汽车 :越野汽车 自卸汽车 :自卸汽车 牵引汽车 :牵引汽车 专用汽车 :专用汽车 客车 :客车 轿车 :轿车 纯电动车 :纯电动车 摩托车 :摩托车 电车 :电车 挂车 :挂车 农用运输车 :农用运输车 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fgoodscode | 税收分类编码 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fgoodsname | 商品名称 | varchar | 100 |  | √ | ' ' | 商品名称 |
| 14 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fproducingarea | 产地 | varchar | 50 |  | √ | ' ' | 产地 |
| 16 | fzzstsgl | 优惠政策类型 | varchar | 80 |  | √ | ' ' | 优惠政策类型,枚举: 免税 :免税 不征税 :不征税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdm_vehicle_info |  | fid |
| 2 | idx_vehicle_info_org |  | forg |
