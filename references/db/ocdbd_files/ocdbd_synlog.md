# 同步日志-ocdbd_synlog

## 同步日志-主表 t_ocdbd_synlog

- **表名称：** 同步日志-主表
- **表名：** t_ocdbd_synlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsyntargetinfo | 目标单摘要 | varchar | 255 |  | √ | ' ' | 目标单摘要 |
| 3 | fsyncode | 同步代码 | bpchar | 1 |  | √ | ' ' | 同步代码,枚举: A :源单不存在 B :分配型数据 C :下推出错 D :下推成功保存出错 E :下推成功提交出错 F :下推成功审核出错 G :下推新增成功 H :无更新目标 I :更新无差异 J :同步成功 K :无删除目标 L :删除反审核目标出错 M :删除撤销目标出错 N :删除目标出错 O :删除目标成功 P :对象锁定中 R :同步出错 |
| 4 | fsynmessage | 同步信息 | varchar | 2000 |  | √ | ' ' | 同步信息 |
| 5 | fsynoperation | 同步操作 | bpchar | 1 |  | √ | ' ' | 同步操作,枚举: A :同步新增 B :同步修改 C :同步删除 D :同步启用 E :同步禁用 |
| 6 | fsyncreatetype | 同步平台 | bpchar | 1 |  | √ | ' ' | 同步平台,枚举: A :事件中心 B :界面操作 |
| 7 | fsynsourceinfo | 源单摘要 | varchar | 255 |  | √ | ' ' | 源单摘要 |
| 8 | fsyntime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 9 | fiscuccess | 同步是否成功 | bpchar | 1 |  | √ | '0' | 同步是否成功 |
| 10 | fsynentitytype | 同步实体类型 | bpchar | 1 |  | √ | ' ' | 同步实体类型,枚举: C :客户同步渠道 M :物料同步商品 A :地址同步渠道地址 B :客户同步渠道地址 D :渠道地址同步客户联系人地址 |
| 11 | fsynuserid | 同步用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_synlog_syntime |  | fsyntime |
| 2 | pk_ocdbd_synlog |  | fid |
