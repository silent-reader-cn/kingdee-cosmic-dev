# 单据同步启停服务日志-cal_stopsyncbillset

## 单据同步启停服务日志-主表 t_cal_stopsyncset

- **表名称：** 单据同步启停服务日志-主表
- **表名：** t_cal_stopsyncset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fstarterid | 启动人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ffailbill_tag | 同步失败单据_详情 | text | 0 |  |  | null | 同步失败单据_详情 |
| 7 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 8 | fstoptype | 启停服务类型 | varchar | 30 |  | √ | 'cal' | 启停服务类型,枚举: cal :按核算组织 inv :按库存组织 |
| 9 | ffailbill | 同步失败单据 | varchar | 255 |  | √ | ' ' | 同步失败单据 |
| 10 | fstarttime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 11 | fstoperid | 停止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 C :即时移动平均法 E :即时先进先出法 D :标准成本法 |
| 13 | fisfinish | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 1 :已启动 0 :已停止 |
| 14 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fstoptime | 停止时间 | timestamp | 0 |  |  | null | 停止时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_stopsyncset |  | fid |
| 2 | idx_cal_stopsync_cma |  | fcalorgid,fmaterialid,faccounttype,fwarehouseid,fstorageorgunitid |
