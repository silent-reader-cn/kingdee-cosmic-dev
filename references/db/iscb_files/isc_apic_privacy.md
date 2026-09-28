# API跨境数据传输策略-isc_apic_privacy

## API跨境数据传输策略-主表 t_iscb_apic_privacy

- **表名称：** API跨境数据传输策略-主表
- **表名：** t_iscb_apic_privacy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fprivacy_info_tag | 数据详情（隐藏）_详情 | text | 0 |  |  | null | 数据详情（隐藏）_详情 |
| 6 | fapi_type | API类别 | varchar | 50 |  | √ | ' ' | API类别,枚举: isc_apic_webapi :WebAPI登记 |
| 7 | fapi_id | 授权API | int8 | 64 |  | √ | 0 | WebAPI登记 isc_apic_webapi |
| 8 | fprivacy_info | 数据详情（隐藏） | varchar | 255 |  | √ | ' ' | 数据详情（隐藏） |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_privacy_c |  | fapi_type,fapi_id |
| 2 | pk_t_iscb_apic_privacy |  | fid |
