# 商旅自助开通-er_autoopened

## 商旅自助开通-主表 t_er_autoopened

- **表名称：** 商旅自助开通-主表
- **表名：** t_er_autoopened

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompanyname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 3 | forderstatusaddr | 订单状态推送地址 | varchar | 2000 |  | √ | ' ' | 订单状态推送地址 |
| 4 | fenableservers | 服务商启用状态 | varchar | 1 |  | √ | ' ' | 服务商启用状态,枚举: 0 :启用 1 :启用失败 2 :已启用 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 |
| 6 | fsynctraceid | 开通traceId | varchar | 255 |  | √ | ' ' | 开通traceId |
| 7 | ftripadminuser | 商旅管理人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsyncadminstatus | 同步管理员 | varchar | 1 |  | √ | ' ' | 同步管理员,枚举: 0 :未同步 1 :已同步 2 :同步失败 |
| 9 | fgrantservers | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: MEITUAN :美团 DIDI :滴滴 CHAILVYIHAO :差旅壹号 XIECHENG :携程 GAODE :高德 |
| 10 | fcompanynum | 公司编码 | varchar | 255 |  | √ | ' ' | 公司编码 |
| 11 | fchannelkeys | 渠道秘钥 | varchar | 255 |  | √ | ' ' | 渠道秘钥 |
| 12 | fsyncusertraceid | 管理员同步traceId | varchar | 255 |  | √ | ' ' | 管理员同步traceId |
| 13 | fchannelid | 渠道ID | varchar | 255 |  | √ | ' ' | 渠道ID |
| 14 | fapprovaltype | 审批方式 | varchar | 1 |  | √ | ' ' | 审批方式,枚举: 0 :申请管控 1 :无申请管控 |
| 15 | fopenedstatus | 开通状态 | varchar | 1 |  | √ | ' ' | 开通状态,枚举: 0 :未开通 1 :已开通 2 :开通失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_autoopened |  | fid |
| 2 | idx_autoopened_company |  | fcompanynum,fcompanyname |
| 3 | idx_autoopened_fservers |  | fgrantservers |
