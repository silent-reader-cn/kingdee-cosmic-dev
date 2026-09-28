# 统计汇总数据-kem_statdata_sum

## 统计汇总数据-主表 t_kem_statdata_sum

- **表名称：** 统计汇总数据-主表
- **表名：** t_kem_statdata_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftime | 统计时间戳 | int8 | 64 |  | √ | 0 | 统计时间戳 |
| 2 | fevtincnt | 事件入队数 | int8 | 64 |  | √ | 0 | 事件入队数 |
| 3 | fsubinstfailcnt | 订阅实例失败数 | int8 | 64 |  | √ | 0 | 订阅实例失败数 |
| 4 | fevttriggerfailcnt | 触发失败数 | int8 | 64 |  | √ | 0 | 触发失败数 |
| 5 | fsubinstignorecnt | 订阅实例忽略数 | int8 | 64 |  | √ | 0 | 订阅实例忽略数 |
| 6 | fevtoutcnt | 事件出队数 | int8 | 64 |  | √ | 0 | 事件出队数 |
| 7 | fsubinsttotalcost | 订阅实例总耗时 | int8 | 64 |  | √ | 0 | 订阅实例总耗时 |
| 8 | fevtid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 9 | fsubid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 10 | fsubinstcnt | 订阅实例数 | int8 | 64 |  | √ | 0 | 订阅实例数 |
| 11 | ftype | 统计时间分类 | int4 | 32 |  | √ | 0 | 统计时间分类,枚举: 1 :时明细 2 :天明细 7 :天汇总数据 9 :总汇总数据 |
| 12 | fsubinstpartsuccnt | 订阅实例部分成功数 | int8 | 64 |  | √ | 0 | 订阅实例部分成功数 |
| 13 | fevttype | 事件类型 | int4 | 32 |  | √ | 0 | 事件类型,枚举: 1 :自定义事件 2 :Webhook 5 :操作事件 0 :默认 |
| 14 | fevttriggercnt | 事件触发数 | int8 | 64 |  | √ | 0 | 事件触发数 |
| 15 | fevttriggersuccnt | 触发成功数 | int8 | 64 |  | √ | 0 | 触发成功数 |
| 16 | fdsid | 数据源ID | int8 | 64 |  | √ | 0 | 数据源ID |
| 17 | fsubinstsuccnt | 订阅实例成功数 | int8 | 64 |  | √ | 0 | 订阅实例成功数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftime | ftime,ftype,fsubid,fevtid,fdsid |
| 2 | ftype | ftime,ftype,fsubid,fevtid,fdsid |
| 3 | fsubid | ftime,ftype,fsubid,fevtid,fdsid |
| 4 | fevtid | ftime,ftype,fsubid,fevtid,fdsid |
| 5 | fdsid | ftime,ftype,fsubid,fevtid,fdsid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_statdata_sum |  | ftime,ftype,fsubid,fevtid,fdsid |
| 2 | idx_kem_statdata_sum_typetime |  | ftype,ftime |
