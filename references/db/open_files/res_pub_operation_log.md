# 资源云操作日志-res_pub_operation_log

## 资源云操作日志-主表 t_pub_operation_log

- **表名称：** 资源云操作日志-主表
- **表名：** t_pub_operation_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeid | 操作对象ID | int8 | 64 |  | √ | 0 | 操作对象ID |
| 3 | fremark | 备注 | text | 0 |  |  | null | 备注 |
| 4 | fname | 操作对象名称 | varchar | 200 |  | √ | ' ' | 操作对象名称 |
| 5 | fcreatorid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | ftype | 操作对象 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fcreatetime | 操作日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作日期 |
| 8 | fnumber | 操作对象编码 | varchar | 200 |  | √ | ' ' | 操作对象编码 |
| 9 | foperationcode | 操作名称 | varchar | 100 |  | √ | ' ' | 操作名称,枚举: save :保存 submit :提交 release :发布 enable :启用 disable :禁用 delete :删除 redo :重做 retry :重试 cancel :撤销 ignore :忽略 invalid :失效 deploy :部署 undeploy :反部署 execute :立即执行 start_flow :立即执行服务流程 terminate :撤销流程实例 edit_var :修改变量 jump :跳转 bar_publish :发布 syncmetaschema :同步数据模型 syncmetalist :同步元数据列表 enable_list :列表启用 resend :数据重发 reconsume :任务重做 form_save :保存 direct_exec :后台任务立即执行 exec_comp :列表执行对比 exec_comp1 :执行对比 creator_retry :发起人重试 creator_redo :发起人重做 re_apply :重新申请 update_solution_detail :资源列表下载 test :测试 restore :还原 save_ext :保存 cancelapply :取消申请 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pub_operation_log_num |  | fnumber |
| 2 | pk_t_pub_operation_log |  | fid |
