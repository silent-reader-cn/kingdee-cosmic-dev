# 消息接收-tsate_msg_receive

## 消息接收-主表 t_tsate_msg_receive

- **表名称：** 消息接收-主表
- **表名：** t_tsate_msg_receive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: |
| 3 | fbusinessid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 4 | ftranseq | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 5 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fnsrsbh | 纳税人识别号 | varchar | 100 |  | √ | ' ' | 纳税人识别号 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fdata | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 10 | ftranid | 消息类型 | varchar | 30 |  | √ | ' ' | 消息类型,枚举: |
| 11 | ftransrc | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_msg_receive |  | fnsrsbh,fskssqq,fskssqz |
| 2 | pk_tsate_msg_receive |  | fid |
